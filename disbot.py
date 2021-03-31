import discord
import random
import asyncio

client = discord.Client()
cmds = ['$hello', '$guess', '$greet']
greets = ['Hi', 'Yo Yo', "What's up", '今日は', 'Bonjour', 'Top of the mornin', 'नमस्ते', 'నమస్కారం']
@client.event
async def on_ready():
  print('Logged in as {}'.format(client.user.name))

@client.event
async def on_message(message):
  if message.author.id == client.user.id:
      return

  if message.content.startswith('$hello'):
      r = random.randint(0, len(greets))
      await message.channel.send(greets[r] + ' <@{}>'.format(message.author.id))

  if message.content.startswith('$greet'):
      r = random.randint(0, len(greets))
      await message.channel.send(greets[r] + ' <@{}>'.format(message.content.split()[-1]))

  if message.content.startswith('$cmds'):
      await message.channel.send('\n'.join(cmds))

  if message.content.startswith('$guess'):
      await message.channel.send('Guess a number between 1 and 10.')

      def is_correct(m):
          return m.author == message.author and m.content.isdigit()

      answer = random.randint(1, 10)

      try:
          guess = await client.wait_for('message', check=is_correct, timeout=5.0)
      except asyncio.TimeoutError:
          return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

      if int(guess.content) == answer:
          await message.channel.send('You are right!')
      else:
          await message.channel.send('Oops. It is actually {}.'.format(answer))


client.run('Enter Token Here')
