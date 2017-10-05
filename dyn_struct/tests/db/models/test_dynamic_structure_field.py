from django.core.exceptions import ValidationError
from django.test import TestCase
from dyn_struct import datatools, factories
from dyn_struct.db.models import DynamicStructure, DynamicStructureField


class BaseModels(TestCase):
    def setUp(self):
        self.dyn_struct = factories.DynamicStructure()
        self.field_struct = factories.DynamicStructureField(structure=self.dyn_struct)


class DynamicStructureFieldTestCase(BaseModels):
    def test_str(self):
        self.assertTrue(self.field_struct.header)
        self.assertEqual(self.field_struct.header, str(self.field_struct))

    def test_str_without_header(self):
        self.field_struct.header = ''
        self.field_struct.name = 'test_name'
        self.field_struct.save()
        self.assertFalse(self.field_struct.header)
        self.assertEqual(self.field_struct.name, str(self.field_struct))

    def test_unicode(self):
        self.assertTrue(self.field_struct.header)
        self.assertEqual(self.field_struct.header, self.field_struct.__unicode__())

    def test_unicode_without_header(self):
        self.field_struct.header = ''
        self.field_struct.name = 'test_name'
        self.field_struct.save()
        self.assertFalse(self.field_struct.header)
        self.assertEqual(self.field_struct.name, self.field_struct.__unicode__())

    def test_get_transliterate_name(self):
        self.field_struct.name = 'тест'
        self.field_struct.save()
        self.assertEqual('test', self.field_struct.get_transliterate_name())

    def test_get_transliterate_name_check_space(self):
        self.field_struct.name = 'test name'
        self.field_struct.save()
        self.assertEqual('test_name', self.field_struct.get_transliterate_name())

    def test_is_header_true(self):
        self.field_struct.header = 'test_header'
        self.field_struct.save()
        self.assertTrue(self.field_struct.is_header())

    def test_is_header_false(self):
        self.field_struct.header = ''
        self.field_struct.save()
        self.assertFalse(self.field_struct.is_header())

    def test_clean_is_header_true_with_name(self):
        self.field_struct.header = 'test_header'
        self.field_struct.name = 'test_name'
        self.field_struct.save()
        with self.assertRaises(ValidationError) as ex:
            self.field_struct.clean()
        self.assertIn('Если указывается заголовок, '
                      'то поля "Название", "Поле" и "Виджет" указывать не нужно', ex.exception)

    def test_clean_is_header_true_with_form_field(self):
        self.field_struct.header = 'test_header'
        self.field_struct.form_field = 'CharField'
        self.field_struct.name = ''
        self.field_struct.save()
        with self.assertRaises(ValidationError) as ex:
            self.field_struct.clean()
        self.assertIn('Если указывается заголовок, '
                      'то поля "Название", "Поле" и "Виджет" указывать не нужно', ex.exception)

    def test_clean_is_header_true_with_widget(self):
        self.field_struct.header = 'test_header'
        self.field_struct.form_field = 'TextInput'
        self.field_struct.name = ''
        self.field_struct.widget = 'CharField'
        self.field_struct.save()
        with self.assertRaises(ValidationError) as ex:
            self.field_struct.clean()
        self.assertIn('Если указывается заголовок, '
                      'то поля "Название", "Поле" и "Виджет" указывать не нужно', ex.exception)

    def test_clean_is_header_false_without_name(self):
        self.field_struct.header = ''
        self.field_struct.name = ''
        self.field_struct.save()
        with self.assertRaises(ValidationError) as ex:
            self.field_struct.clean()
        self.assertIn('Необходимо указать название', ex.exception)
        self.assertEqual('invalid', ex.exception.code)

    def test_clean_is_header_false_without_form_field(self):
        self.field_struct.header = ''
        self.field_struct.name = 'test'
        self.field_struct.form_field = ''
        self.field_struct.save()
        with self.assertRaises(ValidationError) as ex:
            self.field_struct.clean()
        self.assertIn('Необходимо указать поле', ex.exception)
        self.assertEqual('invalid', ex.exception.code)

    def test_build(self):
        self.field_struct.build()