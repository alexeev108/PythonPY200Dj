from django import forms

class TemplateForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

"""
Типы полей и их аналоги задаваемые в формах HTML

* forms.CharField() - обычное поле в html <input type='text'>
* forms.EmailField() - <input type="email">
* Поле для пароля (forms.CharField(widget=forms.PasswordInput) - <input type="password">
* forms.CharField(widget=forms.Textarea) - поле для многострочного ввода <textarea></textarea>
* forms.CharField(widget=forms.HiddenInput) - скрытое поле <input type="hidden">

* forms.IntegerField() - <input type="number">
* forms.DecimalField() - <input type="number" step="any">
* forms.FloatField() - <input type="number" step="any"> (аналогично DecimalField, но для чисел с плавающей точкой в Python)

* forms.BooleanField() - <input type="checkbox">
* forms.NullBooleanField() - <input type="checkbox"> (с тремя состояниями: true, false, null)

* forms.ChoiceField(choices=CHOICES) - <select><option value="value1">Choice1</option><option value="value2">Choice2</option></select>
* forms.TypedChoiceField(choices=CHOICES) - Аналогичен ChoiceField, но с приведением типов выбранного значения.
* forms.MultipleChoiceField(choices=CHOICES) - <select multiple="multiple"><option value="value1">Choice1</option></select>

* forms.FileField() - <input type="file">
* forms.ImageField() - <input type="file" accept="image/*">

* forms.DateField() - <input type="date">
* forms.DateTimeField() - <input type="datetime-local">
* forms.TimeField() - <input type="time">
* forms.DurationField() - <input type="text"> (для ввода продолжительности времени, используется строковое представление)
* forms.SplitDateTimeField() - Два поля ввода: <input type="date"> и <input type="time"> (для ввода даты и времени отдельно)

* forms.URLField() - <input type="url">
* forms.SlugField() - <input type="text"> (обычно используется для ввода "slug" URL, состоящего из букв, цифр, дефисов или подчёркиваний)
* forms.RegexField(regex='[А-яA-z]+') - <input type="text"> (с дополнительной валидацией на стороне сервера для соответствия регулярному выражению)
* forms.UUIDField() - <input type="text"> (для ввода UUID)
"""