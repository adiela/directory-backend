from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    """Ensure the models are updated with the requesting user."""

    def perform_create(self, serializer):
        """Ensure we have the authorized user for ownership."""
        serializer.save(created_by=self.request.user, updated_by=self.request.user)

    def perform_update(self, serializer):
        """Ensure we have the authorized user for ownership."""
        serializer.save(updated_by=self.request.user)
