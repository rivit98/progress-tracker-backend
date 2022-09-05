from datetime import datetime

import bs4
import requests

from crackmes.models import ScrapperHistory, Task


class CrackmesScrapper:
    BASE_URL = "https://crackmes.one/lasts/"

    def __init__(self):
        self.tasks = []
        self.session = requests.Session()

    def start(self):
        page_nr = 1
        while True:
            scrapped_tasks = self.scrap(page_nr)
            if not scrapped_tasks:
                break

            self.tasks.extend(scrapped_tasks)
            page_nr += 1

    def scrap(self, page_number):
        scrapped_tasks = []
        link = self.BASE_URL + str(page_number)

        result = self.session.get(link)
        if result.status_code != 200:
            return scrapped_tasks

        bs = bs4.BeautifulSoup(result.content, "html.parser")
        trs = bs.find_all("tr", class_="text-center")
        # print(f'{link} - {len(trs)}')

        for tr in trs:
            td = list(tr.find_all('td'))
            a = td[0].find('a', href=True)
            td_s = list(map(lambda t: t.text.strip(), td))

            item = dict()
            item['name'] = td_s[0]
            item['hexid'] = a['href'].replace('/crackme/', '')
            item['language'] = td_s[2]
            item['date'] = td_s[7]
            item['writeups_num'] = int(td_s[8])
            item['comments_num'] = int(td_s[9])

            item['date'] = datetime.strptime(item['date'].split(' ')[2], "%m/%d/%Y")
            item['id'] = int(item['hexid'][:8] + item['hexid'][-6:], 16)  # don't ask ...
            scrapped_tasks.append(Task(**item))

        return scrapped_tasks

    def save(self):
        # print(f"Scrapped: {len(self.tasks)} tasks")

        db_tasks = Task.objects.all()
        db_tasks_ids = list(map(lambda t: t.id, db_tasks))
        db_tasks_ids = set(db_tasks_ids)
        scrapped_ids = set(list(map(lambda t: t.id, self.tasks)))
        if len(scrapped_ids) != len(self.tasks):
            ScrapperHistory.objects.create(
                total_scrapped=len(scrapped_ids) - len(self.tasks)
            )
            return

        task_dict = {t.id: t for t in self.tasks}
        origin_task_dict = {t.id: t for t in db_tasks}

        to_create = [task_dict[x] for x in scrapped_ids - db_tasks_ids]
        to_delete = list(db_tasks_ids - scrapped_ids)

        to_update = []
        for tid in [x for x in db_tasks_ids & scrapped_ids]:
            orig_t: Task = origin_task_dict[tid]
            scrapped_t: Task = task_dict[tid]

            if orig_t.writeups_num != scrapped_t.writeups_num or orig_t.comments_num != scrapped_t.comments_num:
                to_update.append(scrapped_t)

        # print(f"to_create {len(to_create)}")
        # print(f"to_update {len(to_update)}")
        # print(f"to_delete {len(to_delete)}")

        history_entry = ScrapperHistory.objects.create(
            total_scrapped=len(self.tasks),
            created=len(to_create),
            updated=len(to_update),
            deleted=len(to_delete)
        )

        Task.objects.bulk_update(to_update, ['writeups_num', 'comments_num'])
        Task.objects.bulk_create(to_create)
        Task.objects.filter(id__in=to_delete).delete()

        history_entry.success = True
        history_entry.save()


def scrap_crackmes():
    p = CrackmesScrapper()
    p.start()
    p.save()
