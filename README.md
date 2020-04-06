# DAILY : A Process for tracking time.
This is my process currently for keeping track of my work related time. I developed it because I did not enjoy the overhead of other tracking applications and I wanted to keep the time and differences tracked in git. I also added and will continue to improve the parser to get more meaningful data out of the logs. 

## How to use?
Simply create a file in this directory for each day you wish to track. Do not add a file extension. 

### File Names
Use `<FOUR DIGIT YEAR>-<TWO DIGIT MONTH>-<DAY OF MONTH>` format for file names.

### Entries / Rows
Use military time: `<TWO DIGIT HOUR>:<TWO DIGIT MINUTE>` in format `<START TIME> - <END TIME> : <PROJECT KEY> - <DESCRIPTION>`

### Example
Filename: `2020-04-05`
Rows:
```
15:30 - 19:30 : PARSER - script time analysis.
19:30 - 20:30 : PARSER - work on parser app, publish to github.
```
## Analysis
So the goal of this is to be able to answer questions like these below:

* How many hours have I worked total?
* How many hours did I work on X topic in Y period?
* When did I start work during Y period?
* When did I stop working during Y period?
* What time of day do I usually work on X topic?

It can only answer the first one right now. 
