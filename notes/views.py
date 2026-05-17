from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Note
from .serializers import RegisterSerializer, NoteSerializer


#  REGISTER 
class Register(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# NOTES LIST + CREATE 
class NoteList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Note.objects.filter(user=request.user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  NOTE DETAIL + UPDATE + DELETE
class NoteDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return Note.objects.get(id=pk, user=user)

    
    def get(self, request, pk):
        try:
            note = self.get_object(pk, request.user)
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        try:
            note = self.get_object(pk, request.user)
            serializer = NoteSerializer(note, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    #
    def delete(self, request, pk):
        try:
            note = self.get_object(pk, request.user)
            note.delete()
            return Response({"message": "Deleted successfully"})

        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)