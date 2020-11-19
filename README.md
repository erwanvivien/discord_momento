![Momento logo](/docs/momento.png)

## How does it work?
The bot gathers ICS data (to understand iCalendar format files) from EPITA scheduling platform Chronos. Then by parsing these we can assemble pictures.

## Why is the bot showing wrong data?
The data the bot stores is updated every 10 minutes. Though we could raise that rate, we prefer not as we estimate it highly sufficient for this purpose. Increasing it would burden the Chronos API and may prevent us from accessing it.

## Disclaimer
*This project includes the work from the following repository: github.com/TheToto/chronos-ics. This wrapper allows to easily retrieve Chronos data.*
