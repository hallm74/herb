from django import forms
from .models import Herb
from .utils import search_unsplash

class HerbAdminForm(forms.ModelForm):
    search_unsplash = forms.CharField(
        required=False,
        label="Search Unsplash for Image",
        help_text="Enter a query to search Unsplash for an image."
    )
    unsplash_choices = forms.ChoiceField(
        required=False,
        label="Select Unsplash Image",
        choices=[],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Herb
        fields = ['name', 'scientific_name', 'description', 'image', 'unsplash_image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize 'unsplash_choices' as empty
        self.fields['unsplash_choices'].choices = []

    def clean(self):
        cleaned_data = super().clean()
        query = cleaned_data.get('search_unsplash')

        if query:
            # Fetch Unsplash results dynamically
            unsplash_results = search_unsplash(query)
            if unsplash_results:
                self.fields['unsplash_choices'].choices = [
                    (image['urls']['regular'], image.get('alt_description', 'No description available'))
                    for image in unsplash_results
                ]
            else:
                # Add an error if no results are found
                self.add_error('search_unsplash', "No results found on Unsplash. Try another query.")
        else:
            # Reset choices if no query is provided
            self.fields['unsplash_choices'].choices = []

        return cleaned_data

def save(self, commit=True):
    herb = super().save(commit=False)

    selected_image_url = self.cleaned_data.get('unsplash_choices')
    print(f"Saving Unsplash URL: {selected_image_url}")  # Debugging output

    if selected_image_url:
        herb.unsplash_image_url = selected_image_url
    else:
        herb.unsplash_image_url = None

    if commit:
        herb.save()
    return herb