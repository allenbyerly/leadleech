# leadleech
scraper used to extract leads from various sources


leadleach is a python script used to generate leads by scraping sources for leads based on pre-determined rules.

//Run a search daily for predefined lists of PEOs and keywords.
//Need name of company, link to posting and the PEO or keyword added to
//a google doc.

## requirements
1. Install Python
For instructions go to: [Installation Instructions](https://github.com/pettarin/python-on-windows/)

2. Install BeautifulSoup
Once Python is installed download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run 
```
$ python get-pip.py
```



### Step 1: Download The Installer

First, open your Web browser and go to [https://python.org/](https://python.org/):

![Python home page](imgs/010_pythonorg.png)

Click on the **Download > Latest Python 3.6.0** link.

You will get a page listing all the new features of Python 3.6.0:

![Python 3.6.0 download page](imgs/020_download.png)

Scroll down until you see the list of available downloads:

![Python 3.6.0 downloads](imgs/021_download.png)

If you have a recent Windows computer,
very likely it is a 64-bit machine,
so you should download the file labeled **Windows x86-64 executable installer**,
and save it on your Download folder or on your Desktop:

![Python 3.6.0 downloads](imgs/030_downloaded.png)

Downloading the file will take from few seconds to a few minutes,
depending on the bandwidth of your Internet connection.

(If you have an older PC that you know is a 32-bit computer,
download the **Windows x86 executable installer** instead.
You can tell whether your PC is a 32-bit or a 64-bit machine
by reading the **System Information** in the **Windows Control Panel**.)

### Step 2: Install Python

Double-click on the file you just downloaded
to start the installation wizard:

![Python 3.6.0 installer](imgs/040_installer.png)

By default, the **Add Python 3.6 to PATH** option is disabled,
but **you should select it**,
as it makes running Python programs much much easier.

Most users should click the **Install Now** button,
which installs Python with the default settings.
(If you want to personalize your installation
or you are told to enable some advanced features,
click on the **Customize installation** option instead.)

The installer might ask you for administrative privileges
or for confirmations like the following:

![Python 3.6.0 installer asking for confirmation](imgs/041_installer.png)

You can safely answer **Yes**.

A progress bar will appear:

![Python 3.6.0 installer progress bar](imgs/042_installer.png)

until the installation completes with the following message:

![Python 3.6.0 installer completed](imgs/043_installer.png)

Starting with Python 3.6.0,
it is recommended to click on
the **Disable path length limit** option,
before closing the installer.
If you do so, you will get a final confirmation dialog:

![Python 3.6.0 installer completed](imgs/044_installer.png)

You can terminate the installation by clicking the **Close** button.

Congratulations, you have **your first Python installation** under your belt!


## Using The Command Prompt

Most Python programs are command line interface (CLI) utilities,
which means that they are not operated
via a graphical user interface (GUI),
also known as "the program window".
Instead, they must be executed
in the **Command Prompt** of Windows,
also known as "shell" or "terminal".

Running a CLI program means
**typing a command string on the Command Prompt of Windows**,
following a certain syntax
which depends on what the program is supposed to do.
You can think of this act as reciting the "right spell"
to get your job done.

### Opening A Command Prompt

To open the Command Prompt,
locate the Command Prompt icon in your Start menu
(or use the search bar):

![Command Prompt icon](imgs/100_cp.png)

Click on the icon. A black window appears:

![Command Prompt window](imgs/101_cp.png)

The first two lines printed in the window
show the version of the Command Prompt.
The last line, which reads ``C:\Users\IEUser>`` in the screenshot above,
is the **prompt**, where you can actually type commands.

The prompt line always starts
with the location of the **working directory**,
that is, the folder where the command prompt is currently acting upon
(``C:\Users\IEUser`` in the screenshot above),
and ends with the ``>`` character.

The prompt normally opens in the **home directory** of the current user:
in fact, we are in ``C:\Users\IEUser``,
because the user is called ``IEUser``.
If your Windows username is ``Olga``,
it is likely you will see
``C:\Users\Olga`` instead.

(Different versions of Windows might have different paths for home directories.)

In the documentation of Python programs you might find a ``$`` character
before examples of commands, as follows:

```
$ python my_awesome_program.py
```

because on Linux and Mac OS X machines
the terminal prompt is usually a ``$`` character.

You should **not** type the ``$`` character,
it is just a placeholder for your actual prompt.
For any practical purpose,
you can mentally replace the ``$`` with your actual prompt,
like ``C:\Users\IEUser>`` in the example above,
as if the documentation was as follows:

```
C:\Users\IEUser> python my_awesome_program.py
```

(You will actually type only ``python my_awesome_program.py`` and
hit the Enter/Return key.)

### The Three Safety Rules

By issuing commands on the Command Prompt,
you can **accidentally delete** your own files or **damage** Windows,
so you must **be careful**.

Do not be afraid or discouraged:
you do not stop using knives just because
you can cut your fingers with them!

By following **Three Safety Rules**,
you can operate the prompt safely:

1. Never issue a command without understanding what it does,
   and only run programs obtained from developers that you trust.
2. If anything happens in the prompt that you do not understand,
   you can simply click on the "X" on the right top corner
   to close the Command Prompt window
   (and hopefully nothing bad will happen to your files).
3. Always copy your Python program in a separate
   folder, and always make copies of your input files in it,
   so that you can just throw away the Python program folder
   if something goes wrong, and start over.

### Changing The Working Directory (``cd``)

As said above, the command prompt normally opens
in the home directory of your user:

![Command Prompt window](imgs/101_cp.png)

If you want to change the current working directory,
you can use the ``cd`` command.
For example, to move to the ``C:\`` directory
(the root directory of your ``C:`` drive),
you type ``cd C:\``
and press the Enter/Return key:

![Command Prompt window](imgs/110_cp.png)

Notice that the prompt changed to ``C:\>``.

### Listing The Contents Of The Working Directory (``dir``)

If you want a list of the files or subdirectories
contained in the current working directory,
issue the ``dir`` command, without arguments:

![Command Prompt window](imgs/111_cp.png)

The prompt shows a list of directories and files
that are contained in the ``C:`` drive:
in the above screenshot they are
``BGinfo``, ``PerfLogs``, ..., ``Windows``.

At this point, if you want to enter the ``Users`` directory,
you can simply type ``cd Users``, and so on.

If you want to go up one level, type ``cd ..``
(two full stop character).
For example, if you are in ``C:\Users\`` and give a ``cd ..``,
you will end up in ``C:\``.

If you want to clear the prompt window, use the ``cls`` command.

### Checking That Python Is Installed Correctly

If you selected the **Add Python to PATH** option,
you can run the Python interpreter (and any Python program)
from any current working directory.

To check this, give the ``python --version`` command:

![Python non-interactive execution](imgs/120_python.png)

The Python version will be printed
(e.g., ``Python 3.6.0``)
and you will get back to the Windows prompt.
You just ran Python in **non-interactive mode**,
meaning that you provided a precise command
("Python, print the version number you are"),
the Python interpreter performed what you asked for,
and then it returned control to the Command Prompt of Windows.

The **non-interactive mode** is how most Python programs work.

If you forget to add the ``--version`` parameter
after the ``python`` command,
you will enter the **interactive Python shell** instead:

![Entering Python interactive shell](imgs/121_python.png)

Notice how the prompt changed to ``>>>``.

To exit the Python shell, and return to the Command Prompt,
just type ``quit()`` and hit the Enter/Return key:

![Leaving Python interactive shell](imgs/122_python.png)

Discussing the interactive shell is beyond the scope of this guide,
since **most programs you are interested in are non-interactive**.


## Running A Python Program

Excellent, now you have all the tools required
to run a Python program on the command line.

As an illustration,
I will use my simple Python script
[``export-kobo``](https://github.com/pettarin/export-kobo/),
which reads annotations and highlights
from the database file of a Kobo eReader device (``KoboReader.sqlite``),
and prints them on the prompt or exports them to an output file.

### Step 1: Download The Source Code

First, download the source code of the Python program you want to run.

This usually implies **downloading** either **a single Python source code** file
(with extension ``.py``), or **a ZIP file containing several Python source code files**
and other resource files that you need to uncompress somewhere on your disk.

The exact details depend on your Python program,
hence be sure to **carefully read its install documentation**.
You can download the prescribed files with your browser,
and then copy/uncompress them using the Windows graphical file manager.

In our example, we download the raw file
[``export-kobo.py``](https://raw.githubusercontent.com/pettarin/export-kobo/master/export-kobo.py)
from the GitHub repository.

Remember **Safety Rule 3**
("copy your Python files into a separate folder")?

We put the downloaded ``export-kobo.py`` file
in a new folder ``C:\export-kobo``:

![Running a Python program](imgs/130_example.png)

Note that we also copied
the ``KoboReader.sqlite`` file
(the input of our Python program)
from our Kobo eReader
to the same folder.

### Step 2: Open A Command Prompt And ``cd`` There

Then, open a Command Prompt as explained above,
and change the current working directory to the folder
where you put your Python program source files.

In our example, ``cd C:\export-kobo``:

![Running a Python program](imgs/130_example.png)

A simpler alternative to using the ``cd`` command
takes advantages of the Windows file explorer.
Just navigate the file explorer to the folder
where your Python code is:

![Opening a prompt from file explorer](imgs/140_opendir.png)

and select the
``File > Open command prompt > Open command prompt``
menu:

![Opening a prompt from file explorer](imgs/141_opendir.png)

you will get a new Command Prompt window,
already located at the correct directory:

![Opening a prompt from file explorer](imgs/142_opendir.png)

### Step 3: Run The Python Program

At this point, we are ready to run our program.

Type ``python export-kobo.py KoboReader.sqlite --list`` and hit Enter/Return:

![Running a Python program](imgs/131_example.png)

The Python interpreter will load our ``export-kobo.py`` program,
and run it with arguments ``KoboReader.sqlite`` and ``--list``.

Clearly, **the semantics of the arguments vary from program to program**,
depending on what each program is supposed to do.

In our case, ``export-kobo.py`` will read the file
whose name is passed as the first parameter (``KoboReader.sqlite``)
and it will list (``--list`` option) the titles of all the eBooks
with annotations or highlights in the database.

If we specify different command arguments, for example
``python export-kobo.py KoboReader.sqlite --csv --output exported.csv``,
we will get a different behavior:

![Running a Python program](imgs/132_example.png)

In particular, this second command exported all the information
contained in the ``KoboReader.sqlite`` file into
the newly created file named ``exported.csv`` in CSV format:

![Running a Python program](imgs/133_example.png)

You must **check the documentation** of your Python program
to know the semantics of its arguments.

Usually, if you run a Python program without arguments
you will get a synopsis of the accepted arguments:

![Running without arguments shows the synopsis](imgs/150_help.png)

If a ``-h`` or ``--help`` argument is given,
then a more verbose help message will be printed:

![Running with -h shows an help message](imgs/151_help.png)




**Congratulations, now you should be able
to download and run a Python program on your own!**


## Acknowledgments

* **Louise Schofield nee Stokes** for suggesting using the file explorer menu
  to open the command prompt at a given directory