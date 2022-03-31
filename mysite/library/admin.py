from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, BookReview

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    can_delete = False
    extra = 0 # išjungia placeholder'ius

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'reader', 'status')
    list_filter = ('status', 'due_back')
    search_fields = ('id', 'book__title', 'book__summary')
    list_editable = ('due_back', 'reader', 'status')

    fieldsets = (
        ('Availability', {
            'fields': ('book', 'status', 'due_back', 'reader')
        }),
    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer', 'content')


admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)