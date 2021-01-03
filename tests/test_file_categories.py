from unittest import TestCase
from ddt import ddt, data, unpack
from src.file_type_specifier import FileCategory
from tests.category_test_data import category_test_data_01


@ddt
class TestFileCategory(TestCase):
    @data(*category_test_data_01['expected_results'])
    @unpack
    def test_get_file_category(self, extension, category):
        file_category = FileCategory(category_test_data_01['categories'])
        actual_category = file_category.get_file_category(extension)

        self.assertEqual(category, actual_category)

