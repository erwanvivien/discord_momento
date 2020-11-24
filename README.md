![Momento logo](/docs/momento.png)

Momento is a Discord bot retrieving ICS feed from [iChronos](https://ichronos.net/) website to make it accessible from Discord with simple commands. It allows students to check their schedule whenever they want with great simplicity and accessibility.

## How does it work?
The bot gathers ICS data (to understand iCalendar format files) from EPITA scheduling platform Chronos. Then by parsing these we can assemble pictures.

## How to use it?
Invite the bot on your server through [this link](https://discord.com/). Type `mom?help` to get a list of the available features. Here is an exhaustive list of all the features.

- `mom?set <group>` - sets your default group (so that you don't have to specify it each time)
- `mom?prefix <group>` - changes your ``?`` personally
- `mom?clear` - clears user settings from database (prefix and default group)
- `mom?report <message>` - reports a bug to the devs (it has to be at least 70-characters long)
- `mom?next [group]` - shows the very next lesson of the day
- `mom?week [group]` - shows week's schedule
- `mom? [group]` - shows today's schedule
- `mom?help` - shows bot help information

If you feel like contacting us for other things than technical, find our mail addresses right below. Otherwise, please use the report command right above.

## Why is the bot showing wrong data?
The data the bot uses comes from iChronos website, which is only updated once a day. We are aiming to move to the official Chronos API as soon as we gather more information about how it works. We are in close contact with the people responsible for its operation. The transition will be smooth and may take some time.

## Authors
- Hugo BOIS (*hugo.bois@epita.fr*)
- Erwan VIVIEN (*erwan.vivien@epita.fr*)

## Disclaimer
*Momento is not associated with EPITA or Ionis Education Group. Its use comes with absolutely no guarantee.*