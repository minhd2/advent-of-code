from absl.testing import absltest
from absl.testing import parameterized
from main_two import valid_adapters

class ValidAdaptersTest(parameterized.TestCase):
	@parameterized.named_parameters(
		{
			'testcase_name': 'Test A',
			'input': [1,3,4,6],
			'want': 5,

		},
		{
			'testcase_name': 'Test B',
			'input': [1,3,4,6,8],
			'want': 5,
		},
		{
			'testcase_name': 'Test C',
			'input': [3,4,5,8],
			'want': 2,
		},
		{
			'testcase_name': 'Advent Test',
			'input': [1,4,5,6,7,10,11,12,15,16,19],
			'want': 8,
		},

		)
	def testVariations(self, input: list(), want: int):

		self.assertEqual(valid_adapters(input), want)

