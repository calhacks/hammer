ANNOTATOR_ID = 'annotator_id'
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
SETTING_WAVE = '0' # boolean
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to the judging portion of Hack The Impact. Remember that
for your project to be eligble for prizes, you must judge at least 
five of your fellow participants' projects.

**Please read this important message carefully before continuing.**

Hammer is a fully automated peer-to-peer expo judging system that both 
tells you where to go and collects your votes.

You will be able to judge projects on Hammer during your wave (see the top 
of the page). Organizers will announce the start of each wave, please listen 
carefully for your wave's announcement. At all other times, you should be 
demo-ing your projects to your peers and sponsors at your table.

The system is based on the model of pairwise comparison. You'll start off by
looking at a single submission, and then for every submission after that,
you'll decide whether it's better or worse than the one you looked at
**immediately beforehand**.

If at any point, you can't find a particular submission, you can click the
'Skip' button and you will be assigned a new project. **Please don't skip
unless absolutely necessary.**

Hammer makes it really simple for you to submit votes, but please think hard
before you vote. **Once you make a decision, you can't take it back**.
'''.strip()

DEFAULT_EMAIL_SUBJECT = '[IMPORTANT] Hack for Impact Judging Information'

DEFAULT_EMAIL_BODY = '''
Hi {name},

Thanks for submitting to Hack for Impact! We're doing judging a little
different this year. We'll be having participants judge each others projects.

To be eligble for prizes, you must judge at least five of your fellow participants'
projects.

Judging will be done using Hammer, an online platform for expo judging built
by the Cal Hacks team. 

To access the system, visit {link}.

DO NOT SHARE this email with others, as it contains your personal magic link.

Once you're in, please take the time to read the welcome message and
instructions before continuing.
'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again.
'''.strip()

DEFAULT_PRESENTING_MESSAGE = '''
At the moment, your wave is presenting their projects.

Please head to your table to demo your projects to other hackers.

(Remember, to win prizes, you need to be judged!)
'''.strip()

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open the magic link emailed to you to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
We couldn't find a project for you to judge.

Wait for a little bit and reload the page to try again.

If you've looked at all the projects already, then you're done.
'''.strip()
