## Scenario ##

You want to build a auto-house with all you appliances designed to make your life easier.
For example, everyday in the morning, when you snooze the alarm, the alarm clock tells the coffee maker to start brewing, 
with different type of cookie everyday. 

But as time goes by, you realize you could really use some new features, for instance, alarm skips weekends, 
and so does the coffee maker; turn off the sprinkler 10 minutes before shower; set the alarm early in trash days, etc.

The system could be very complex if we keep on having each object communicate directly with each other. 
It will be hard to keep track of which rules reside in which objects too.

## Solution ##
We could use the Mediator Pattern.
Adding a mediator increases the reusability of the objects supported by the Mediator by decoupling them from the system.
It simples maintenance of the system by centralizing control logic, as well as reduces the variety of the message sent between
objects in the system. 