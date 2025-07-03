from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note
from .forms import NoteForm

def note_list(request):
    """
    Display a list of all notes
    """
    notes = Note.objects.all() # type: ignore
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_create(request):
    """
    Handle creation of a new note
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('notes:note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Create Note'})

def note_edit(request, pk):
    """
    Handle editing of an existing note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('notes:note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Edit Note'})

def note_delete(request, pk):
    """
    Handle deletion of a note
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('notes:note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note}) 