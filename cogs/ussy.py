import discord
from discord.ext.commands import Cog
import re

def setup(bot: discord.Bot):
	bot.add_cog(Ussy(bot))

class Ussy(Cog):
	"""Negative reinforcement for alph's brain"""
	def __init__(self, bot: discord.Bot):
		self.bot: discord.Bot = bot
		print("Initialized Ussy cog")

	@Cog.listener()
	async def on_message(self, message: discord.Message):
		if message.author.id == self.bot.user.id:
			return
		r = re.compile(
			r'''
			\b[a-zA-Z]*ussy\b
			''',
			re.VERBOSE | re.IGNORECASE
			)
		matches = set(r.findall(message.content))
		check = matches - set([
			# Special cases
			'cyberbussy', # This bot's nickname includes "ussy"
			# 4 letter words
			'ussy', # we need a way to refer to the bare suffix
			'-ussy',
			# 5 letter words
			'bussy', # This is a word now, albeit the one that started the trend
			'cussy', # From "cuss", i.e. using offensive language
			'fussy',
			'gussy',
			'hussy',
			'jussy', # A commune in france and a municipality in geneva switzerland
			'mussy', # Having been mussed; messy, rumpled; (2) "mercy" in AAVE
			'pussy',
			'sussy', # More sus than ussy, it gets the trash emoji already
			'wussy',
			# 6 letter words
			'moussy', # Having the qualities of mousse
			# 7 letter words
			'ampussy', # Obsolete term for "ampersand" (&)
			'mucussy', # Full of mucus
			'chaussy', 
			'debussy',
			'proussy',
			'unfussy',
			'virussy', # Full of or similar to viruses
			# 8 letter words
			'asspussy', # Vulgar slang highlighting the fuckability of the anus
			'ass-pussy',
			'boipussy', # same as above
			'boi-pussy',
			'boypussy', # same as above
			'boy-pussy',
			'circussy', # resembling a circus
			'citrussy', # having citrus-like qualities
			'henhussy', # a girl who tends chickens
			'manpussy', # same as boypussy
			'man-pussy',
			'nonfussy',
			# 9 letter words
			'octopussy', # similar to an octopus
			'overfussy',
			# 10 letter words
			'mouthpussy', # like "asspussy" but for the mouth
			'superpussy',
			'tussymussy', # Alternate spelling of tussie-mussie, historically used in Victorian times to refer to a nosegay* given by one person to another to convey a message in the language of flowers**. *nosegay = like a small bouquet of flowers intended to be put up to your nose and smelt, **language of flowers = floriography
			'tussy-mussy',
			# 11 letter words
			'pocketpussy' # Apparently this can be used as one word
		])
		if check:
			await message.reply("https://media.discordapp.net/attachments/809278919815200810/955624419219369994/ussy.jpg",mention_author=False)
