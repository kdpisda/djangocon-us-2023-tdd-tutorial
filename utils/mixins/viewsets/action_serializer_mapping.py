class ViewSetActionSerializerMixin:
    # serializer_action_classes = {}

    available_actions = [
        "create",
        "list",
        "retrieve",
        "update",
        "destroy",
        "partial_update",
    ]

    def get_serializer_class(self):
        """
        Determine which serializer class to use based on the current action.
        """
        if getattr(self, "serializer_action_classes"):
            raise NotImplementedError(
                "serializer_action_classes must be defined in the inherited class."
            )

        return self.serializer_action_classes.get(self.action, self.serializer_class)
