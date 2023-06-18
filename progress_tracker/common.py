class CustomSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_action_classes.get(
            self.action, self.serializer_action_classes["default"]
        )
