# purpose

---

The goal of this project is to add another module to the cli fetch _Fastfetch._ I enjoy the aspect of having some of my more pertinent information on display as I open a terminal and the idea of adding personalized weather seemed like an obvious addition.

---

## goal

---

The goal isn’t always to create something but it is always to learn something. I’m sure if I looked, someone has already done this. I decided to make this on my own to learn some different skill sets

- api calls
- JSON imports
- JSON dumps
- Better understanding of conditional statements
  - Case statements
  - For/If statements
  - Using ranges in a list
- Export/import variables and functions
- The Importance of exporting environment variables so as to not expose my own api tokens

---

### progress

---

So far I have accomplished

- Location tracking
  - able to pull IP address to get IP based location to display weather information
    - Looking into how I could refine/be more accurate with that information.
- API
  - successfully calling and API
  - Creating specific variables based on information output
  - handing those variables off to other scripts
- Logic statements
  - Used the information to display the weather conditions in a graphical format
  - Referenced time of day to compare sunrise/sunset to display a sun/moon
  - Used a statement to map ranges to specific numbers to add graphical moon phases when displaying the moon
  <blockquote class="imgur-embed-pub" lang="en" data-id="a/vgN4SER" data-context="false" ><a href="//imgur.com/a/vgN4SER"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
  - Json
  - imported the information
  - Exported the information as JSON
    - trying to figure out how to add this to _fastfetch._
      - I think I might need to pull the source code and build it myself so I can add a module that the configuration file can use.

---

#### outcome

---

As of now, I have the code displaying the information in the terminal. This is only as a reference and will be cleaned to give a more streamlined and useful output.

---

# things to do

---

- look at adding .png images to make the output look better
- make sure dependencies are listed
