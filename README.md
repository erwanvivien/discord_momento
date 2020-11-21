![Momento logo](/docs/momento.png)

Momento is a Discord bot retrieving ICS feed from [iChronos](https://ichronos.net/) website to make it accessible from Discord with simple commands. It allows students to check their schedule whenever they want with great simplicity and accessibility.

## How does it work?
The bot gathers ICS data (to understand iCalendar format files) from EPITA scheduling platform Chronos. Then by parsing these we can assemble pictures.

## How to use it?
Invite the bot on your server through [this link](https://discord.com/). Type `mom?help` to get a list of the available features. Here is an exhaustive list of all the features.

- `mom?set <class>` - sets your default class (so that you don't have to specify it each time)
- `mom?prefix <class>` - changes your ``?`` personally
- `mom?report <message>` - reports a bug to the devs (it has to be at least 70-characters long)
- `mom?next [class]` - shows the very next lesson of the day
- `mom?week [class]` - shows week's schedule
- `mom? [class]` - shows today's schedule
- `mom?help` - shows bot help information

If you feel like contacting us for other things than technical, find our mail addresses right below. Otherwise, please use the report command right above.

## Why is the bot showing wrong data?
The data the bot stores is updated every 10 minutes. Though we could raise that rate, we prefer not as we estimate it highly sufficient for this purpose. Increasing it would burden the Chronos API and may prevent us from accessing it.

## Authors
- Hugo BOIS (*hugo.bois@epita.fr*)
- Erwan VIVIEN (*erwan.vivien@epita.fr*)

## Disclaimer
*Momento is not associated with EPITA or Ionis Education Group. Its use comes with absolutely no guarantee.*