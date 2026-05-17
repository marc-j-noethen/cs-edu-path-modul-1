## 📊 Summary Using the 80/20 Principle

### **Internet vs. World Wide Web: The Difference**

**Often confused, but different**:

```
┌──────────────────────────────────────┐
│          INTERNET                    │  = Infrastructure
│  (Global Network of Computers)      │  = The "Roads"
│                                      │
│  ┌────────────────────────────────┐ │
│  │     WORLD WIDE WEB (WWW)       │ │  = Service on the Internet
│  │  (System of linked            │ │  = The "Addresses & Destinations"
│  │   Hypertext Documents)         │ │
│  └────────────────────────────────┘ │
│                                      │
│  Other Services: E-Mail, FTP, etc.  │
└──────────────────────────────────────┘
```

**Internet** = Network Infrastructure (TCP/IP, Router, Cables) **World Wide Web** = Hypertext System (HTTP, HTML, Web Pages)

**Analogy**: Internet = Road Network | WWW = Addresses and Houses on those Roads

### **Website Types**

**Static Website**:

```
HTML file on server
    ↓
Every visitor sees the same content
    ↓
No database, no user interaction
```

**Examples**: Business card websites, portfolios, info pages

**Dynamic Website**:

```
Server generates content on-the-fly
    ↓
Content based on user/database/time
    ↓
Interactive features
```

**Examples**: Facebook, Amazon, YouTube, news portals

**Today**: We learn the **building blocks** (HTML/CSS), which apply to **both**!

### **How the Web Works: Client-Server Model**

```
┌──────────────┐                      ┌──────────────┐
│   BROWSER    │                      │  WEB SERVER  │
│   (Client)   │                      │              │
└──────┬───────┘                      └──────┬───────┘
       │                                     │
       │  1. HTTP Request                   │
       │  "Give me index.html"              │
       │ ───────────────────────────────────>│
       │                                     │
       │                                     │  2. Server
       │                                     │     finds file
       │                                     │
       │  3. HTTP Response                  │
       │  [HTML, CSS, JS Files]             │
       │ <───────────────────────────────────│
       │                                     │
       │  4. Browser renders page           │
       │     (displays content)             │
       │                                     │
```

**Process**:

1. **User** types URL (e.g. `http://www.example.com`)
2. **Browser** sends **HTTP Request** to **Server**
3. **Server** responds with **HTML/CSS/JS files**
4. **Browser** **renders** (draws) the web page

**Important**: Browser = Software on **your** device | Server = Computer **somewhere** on the Internet

### **HTML: The Structure (the "What")**

**HTML (HyperText Markup Language)** = **Markup language** for web page structure

**Core Concepts**:

#### **Tags (Markings)**

```html
<tagname>
```

- Surrounded by **angle brackets** `< >`
- Usually in **pairs**: `<p>` (opening) and `</p>` (closing)
- Closing tag has a **forward slash** `/`

#### **Elements**

```html
<p>This is a paragraph.</p>
 │              │          │
 │              │          └─ Closing Tag
 │              └──────────── Content
 └─────────────────────────── Opening Tag

Together = ELEMENT
```

**Void Elements** (without closing tag):

```html
<img src="image.jpg" alt="Description">
<br>  <!-- Line break -->
<hr>  <!-- Horizontal line -->
```

#### **Attributes**

```html
<a href="https://google.com">To Google</a>
   │                │
   │                └─ Value
   └──────────────────── Name

Format: name="value"
```

### **HTML Basic Structure: The Skeleton of Every Web Page**

```html
<!DOCTYPE html>                    <!-- Document type: HTML5 -->
<html>                             <!-- Root element -->
<head>                             <!-- Meta area (invisible) -->
    <meta charset="UTF-8">         <!-- Character encoding -->
    <meta name="viewport" 
          content="width=device-width, 
                   initial-scale=1.0">  <!-- Responsive Design -->
    <title>My Page</title>         <!-- Title (browser tab) -->
</head>
<body>                             <!-- Visible content -->
    <h1>Heading</h1>               <!-- Heading -->
    <p>A paragraph of text.</p>    <!-- Paragraph -->
</body>
</html>
```

**Structure Overview**:

```
<!DOCTYPE html>     → Document type declaration
<html>              → Everything inside
  <head>            → Meta information
    <title>         → Page title
  </head>
  <body>            → Visible content
    <h1>, <p>, ...  → Content elements
  </body>
</html>
```

### **Important HTML Tags**

|Tag|Meaning|Example|
|---|---|---|
|`<h1>` to `<h6>`|Headings (1=largest)|`<h1>Main Heading</h1>`|
|`<p>`|Paragraph|`<p>Text here.</p>`|
|`<a>`|Link (Anchor)|`<a href="url">Text</a>`|
|`<img>`|Image|`<img src="image.jpg" alt="Description">`|
|`<div>`|Container (Block-Level)|`<div>Grouped content</div>`|
|`<span>`|Container (Inline)|`<span>Inline text</span>`|
|`<ul>` / `<ol>`|List (unordered/ordered)|`<ul><li>Item</li></ul>`|
|`<li>`|List item|`<li>Point 1</li>`|
|`<br>`|Line break|`Text<br>New line`|
|`<hr>`|Horizontal line|`<hr>`|

**Important Attributes**:

- `href`: Link target (`<a href="...">`)
- `src`: Source (`<img src="...">`)
- `alt`: Alternative text (`<img alt="...">`)
- `class`: CSS class (`<div class="...">`)
- `id`: Unique ID (`<div id="...">`)
- `style`: Inline CSS (`<p style="...">`)

### **CSS: The Styling (the "How")**

**CSS (Cascading Style Sheets)** = **Stylesheet language** for web page appearance

**Separation of Concerns**:

```
HTML → What IS the content?     (Structure, meaning)
CSS  → How does it LOOK?        (Color, layout, font)
```

**CSS controls**:

- 🎨 Colors
- ✍️ Font types and sizes
- 📏 Spacing (Margin, Padding)
- 📐 Layout (Position, Size)
- ✨ Animations

#### **CSS Syntax**

```css
selector {
  property: value;
  property: value;
}
```

**Example**:

```css
p {
  color: navy;
  font-size: 16px;
}

│   │         │
│   │         └─ Value
│   └─────────── Property
└───────────────── Selector (selects elements)
```

**Explanation**: All `<p>` elements get blue text and font size 16 pixels

#### **CSS Selectors**

**Element Selector** (selects all elements of a type):

```css
h1 {
  color: teal;
}
```

→ All `<h1>` become teal

**Class Selector** (selects elements with a specific class):

```css
.highlight {
  background-color: yellow;
}
```

→ All elements with `class="highlight"` get a yellow background

HTML:

```html
<p class="highlight">This text is highlighted</p>
```

**ID Selector** (selects element with a specific ID):

```css
#header {
  font-size: 24px;
}
```

→ Element with `id="header"` gets font size 24px

HTML:

```html
<div id="header">Header content</div>
```

**Important**:

- **Class** (`.`) = Reusable multiple times
- **ID** (`#`) = Only once per page!

### **Including CSS: Three Methods**

#### **1. External CSS (Recommended!)** ✅

**HTML** (`index.html`):

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

**CSS** (`style.css`):

```css
body {
  background-color: lightyellow;
}
```

**Advantages**:

- ✅ Reusable across multiple pages
- ✅ Clean separation
- ✅ Easy to maintain

#### **2. Internal CSS** ⚠️

```html
<head>
  <style>
    body {
      background-color: lightyellow;
    }
    h1 {
      color: green;
    }
  </style>
</head>
```

**Use**: Only for single pages or page-specific styles

#### **3. Inline CSS** ❌ (Avoid!)

```html
<p style="color: red; font-weight: bold;">Red text</p>
```

**Disadvantages**:

- ❌ Mixes structure and style
- ❌ Hard to maintain
- ❌ Not reusable

**Only in exceptional cases!**

### **HTML & CSS Together: Practical Example**

**HTML** (`index.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My First Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Welcome!</h1>
    <p class="intro">This is my first website.</p>
    <p>I am learning HTML and CSS.</p>
</body>
</html>
```

**CSS** (`style.css`):

```css
body {
    background-color: #f0f0f0;  /* Light gray background */
    font-family: Arial, sans-serif;
}

h1 {
    color: dodgerblue;          /* Blue heading */
    text-align: center;         /* Centered */
}

.intro {
    font-weight: bold;          /* Bold text */
    color: darkgreen;           /* Dark green */
}
```

**Result in Browser**:

- Page with light gray background
- Blue, centered heading "Welcome!"
- First paragraph bold and dark green
- Second paragraph normal (Arial font)

### **Creating a Website: Step-by-Step (Windows 11)**

#### **Step 1: Create Folder**

1. Open **File Explorer**
2. Create new folder: `my_website`
3. Navigate into the folder

#### **Step 2: Open VS Code**

1. Start VS Code
2. **File** → **Open Folder** → Select `my_website`

#### **Step 3: Create Files**

1. New file: `index.html`
2. New file: `style.css`

**Folder structure**:

```
my_website/
├── index.html
└── style.css
```

#### **Step 4: Write HTML**

**`index.html`**:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello World!</h1>
    <p>I am learning web development.</p>
</body>
</html>
```

**Save**: `Ctrl + S`

#### **Step 5: Write CSS**

**`style.css`**:

```css
h1 {
    color: dodgerblue;
}

body {
    background-color: #f0f0f0;
}
```

**Save**: `Ctrl + S`

#### **Step 6: Open in Browser**

1. In File Explorer: find `index.html`
2. **Right-click** → **Open with** → **Choose browser** (Chrome, Edge, Firefox)
3. Page is displayed!

**Testing changes**:

1. Change CSS file (e.g. `color: red;`)
2. Save (`Ctrl + S`)
3. **Refresh** browser (`F5` or `Ctrl + R`)
4. See the change!

### **Using Browser Developer Tools**

**View HTML source code**:

1. Open any web page
2. **Right-click** → **View Page Source** / **Inspect**
3. HTML code is displayed

**Open Developer Tools**:

- **Windows**: `F12` or `Ctrl + Shift + I`
- **Right-click** → **Inspect Element**

**What do you see?**

- **Elements**: HTML structure (interactive)
- **Styles**: CSS rules for selected element
- **Console**: JavaScript console (later)
- **Network**: Network requests

**Useful for**:

- Understanding how pages are built
- Debugging your own pages
- Testing CSS live (temporarily)

### **Important CSS Properties (Starter Set)**

**Text Styling**:

```css
color: blue;              /* Text color */
font-size: 20px;          /* Font size */
font-family: Arial;       /* Font type */
font-weight: bold;        /* Bold text */
text-align: center;       /* Alignment */
text-decoration: underline; /* Underline */
```

**Background**:

```css
background-color: yellow; /* Background color */
```

**Spacing**:

```css
margin: 10px;             /* Outer spacing */
padding: 10px;            /* Inner spacing */
```

**Size**:

```css
width: 200px;             /* Width */
height: 100px;            /* Height */
```

**Border**:

```css
border: 1px solid black;  /* Border: thickness, style, color */
```

### **Color Values in CSS**

**Color names** (simple):

```css
color: red;
color: blue;
color: lightgreen;
```

**Hexadecimal** (precise):

```css
color: #FF0000;  /* Red */
color: #00FF00;  /* Green */
color: #0000FF;  /* Blue */
color: #f0f0f0;  /* Light gray */
```

**RGB** (Red, Green, Blue):

```css
color: rgb(255, 0, 0);     /* Red */
color: rgb(0, 255, 0);     /* Green */
color: rgba(0, 0, 255, 0.5); /* Blue, 50% transparent */
```

### **Why Separation of HTML and CSS?**

**Problem without separation**:

```html
<!-- Everything mixed up -->
<p style="color: red; font-size: 16px; margin: 10px;">
  Text with direct styling
</p>
<p style="color: red; font-size: 16px; margin: 10px;">
  The same styling repeated again
</p>
```

**Disadvantages**:

- ❌ Code repetition
- ❌ Hard to maintain (change = every element individually)
- ❌ Cluttered
- ❌ Mixes structure and style

**Solution with separation**:

**HTML** (structure only):

```html
<p class="highlight">Text 1</p>
<p class="highlight">Text 2</p>
```

**CSS** (style only):

```css
.highlight {
  color: red;
  font-size: 16px;
  margin: 10px;
}
```

**Advantages**:

- ✅ Reusable (one rule, many elements)
- ✅ Central change (one place = changed everywhere)
- ✅ Clear overview
- ✅ Clean separation

### **Core Message**

**Web Development** starts with two fundamental pillars:

**HTML** = **Structure** and **Meaning** (the "What")

- Tags, elements, attributes
- Basic framework of every web page
- `<html>`, `<head>`, `<body>`

**CSS** = **Appearance** and **Presentation** (the "How")

- Selectors, properties, values
- Controls colors, fonts, layout
- Separated from HTML (External CSS)

**Working Together**:

```
HTML structures → CSS styles → Browser renders
```

**Client-Server Model**:

- **Browser** (Client) makes request
- **Server** responds with HTML/CSS
- **Browser** displays page

**Best Practice**: **Separation of Concerns**

- HTML for structure
- CSS for style
- Cleanly separated = maintainable + flexible

**Next Steps**: JavaScript (for interactivity) comes later!

**Final analogy**: HTML is like the **skeleton and organs** of a house (structure, rooms, doors), CSS is the **paint, wallpaper, and decoration** (how it looks). Together they make a complete, attractive web page! 🏠🎨💻

---

## Overview Table

|**Category**|**Details**|
|---|---|
|**Tools Used**|• **VS Code** (Visual Studio Code): Code editor (Windows & macOS) - [code.visualstudio.com](https://code.visualstudio.com/)<br>• **Web Browser**: Chrome, Firefox, Safari, Edge (for viewing web pages)<br>• **Browser Developer Tools**: Right-click → "Inspect" / "Inspect Element" (macOS & Windows: F12)<br>• **Finder/File Explorer**: File management (macOS: Finder; Windows: Explorer)<br>• **Notepad++/Sublime Text**: Alternative code editors (Windows)<br>• **TextEdit**: Simple text editor (macOS; Windows: Notepad)<br>• **Live Server Extension**: VS Code extension for local web server<br>• **Emmet**: HTML/CSS quick input in VS Code (pre-installed)<br>• **Git/GitHub**: Version control (optional, for projects)<br>• **Browser Extensions**: Web Developer, ColorZilla, WhatFont<br>• **Validator**: W3C HTML/CSS Validator (online tools)|
|**Technical Terms**|• **Internet**: Global network of computers (infrastructure)<br>• **World Wide Web (WWW)**: Service on the Internet (hypertext system)<br>• **Web Page**: Single web page (one HTML document)<br>• **Website**: Collection of related web pages<br>• **Static Website**: Static web page (fixed content)<br>• **Dynamic Website**: Dynamic web page (generated content)<br>• **Web Browser**: Program for viewing web pages (client)<br>• **Web Server**: Computer that provides web pages (server)<br>• **Client-Server Model**: Client-server model<br>• **HTTP** (HyperText Transfer Protocol): Transfer protocol<br>• **URL** (Uniform Resource Locator): Web address<br>• **Rendering**: Display/drawing of the web page<br>• **HTML** (HyperText Markup Language): Structural language for web pages<br>• **Markup Language**: Markup language<br>• **Tag**: HTML marking (e.g. `<p>`)<br>• **Element**: HTML element (tag + content + closing tag)<br>• **Opening Tag**: Opening tag (e.g. `<h1>`)<br>• **Closing Tag**: Closing tag (e.g. `</h1>`)<br>• **Attribute**: HTML attribute (additional information)<br>• **Value**: Attribute value<br>• **Void Element**: Empty element without closing tag (e.g. `<img>`)<br>• **DOCTYPE**: Document type declaration<br>• **Root Element**: Root element (`<html>`)<br>• **Meta Information**: Meta data (not visible)<br>• **Character Encoding**: Character encoding (UTF-8)<br>• **Viewport**: Display area (for responsive design)<br>• **CSS** (Cascading Style Sheets): Stylesheet language<br>• **Selector**: CSS selector (selects elements)<br>• **Declaration Block**: Declaration block (in `{}`)<br>• **Property**: CSS property (e.g. `color`)<br>• **Value**: CSS value (e.g. `blue`)<br>• **External CSS**: External CSS file (`.css`)<br>• **Internal CSS**: Internal CSS (in `<head>`)<br>• **Inline CSS**: Inline CSS (in `style` attribute)<br>• **Specificity**: CSS specificity (precedence rules)<br>• **Separation of Concerns**: Separation of responsibilities<br>• **Responsive Design**: Adaptive design (various screen sizes)|
|**Important Vocabulary**|• **Infrastructure**: Basic structure/foundation<br>• **Linked**: Connected to each other<br>• **Hypertext**: Text with links to other documents<br>• **Document**: Single file/page<br>• **Collection**: Group of related elements<br>• **Hosted**: Stored/provided on server<br>• **Fixed content**: Unchangeable content<br>• **Dynamically generated**: Created on-the-fly<br>• **Interaction**: User inputs/actions<br>• **Building blocks**: Fundamental components<br>• **Retrieve**: Fetch/get<br>• **Display**: Present/render<br>• **Request**: Request<br>• **Response**: Response<br>• **Process**: Process<br>• **Interpret**: Understand/evaluate<br>• **Mark up**: Mark (markup)<br>• **Structure**: Layout/organization<br>• **Pair**: Matching tags (opening + closing)<br>• **Angle brackets**: Angle Brackets `< >`<br>• **Forward slash**: Forward Slash `/`<br>• **Empty**: Without content (void)<br>• **Name-value pair**: Attribute = "value"<br>• **Anchor**: Link/hyperlink<br>• **Meta information**: Information about the page<br>• **Visible**: Displayed in browser<br>• **Heading**: Heading<br>• **Paragraph**: Paragraph<br>• **Embed**: Insert (embed)<br>• **Alternative text**: Description for screen readers/when image is missing<br>• **Container**: Enclosing element<br>• **Group**: Combine<br>• **Inline**: Within a line<br>• **Block**: Own paragraph<br>• **Source code**: Source code<br>• **Developer tools**: Developer tools<br>• **Hierarchical**: Tree structure<br>• **Representation**: Appearance/presentation<br>• **Appearance**: Look/style<br>• **Colors**: Colors<br>• **Fonts**: Fonts<br>• **Spacing**: Spacing<br>• **Layout**: Arrangement<br>• **Animation**: Animated effects<br>• **Separation**: Separation<br>• **Meaning**: Semantics<br>• **Presentation**: Visual representation<br>• **Maintainable**: Maintainable<br>• **Flexible**: Adaptable<br>• **Cascading**: Cascading (inheritance)<br>• **Rule**: CSS rule<br>• **Declaration**: Declaration<br>• **Semicolon**: Separator `;`<br>• **Class**: Class (`.my-class`)<br>• **ID**: Unique identifier (`#my-id`)<br>• **Link**: Link<br>• **Embed**: Embed<br>• **Refresh**: Refresh (reload page)<br>• **Foundation**: Foundation/base|