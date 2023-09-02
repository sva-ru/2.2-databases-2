from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if self.deleted_forms and self._should_delete_form(form):
                continue
            elif form.cleaned_data.get('is_main'):
                count += 1
            if count > 1:
                raise ValidationError('Is_main should be only one tag')
            elif count == 0:
                raise ValidationError('Assign is_main')

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at']
    inlines = [ScopeInline, ]
    # list_filter = ['published_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # list_display = ['name']
    inlines = [ScopeInline,]


