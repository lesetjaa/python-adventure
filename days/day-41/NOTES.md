# Notes

## How does the Internet Work

- The internet is basically wires connecting computers together. Some of these computers have to be online 24/7, these are called servers. Any computer that is used to access these servers are called clients.

### How the internet accesses or locates websites we need

- When we type `www.google.com`, behind the scenes the browser (client) sen the message to the `ISP (Internet Service Provider, vodacom)`
- The ISP relays the message to the `DNS (Domain Name System)`, this is like a big Phonebook
- The DNS will lookup the exact `IP address (Internet Protocal address)` of the website we are trying to access, Every computer that is connected to the internet has an IP address, it is like a postal code for the computer
- Then the DNS will send back that IP address back to our browser through the ISP then we can make the direct request to that IP address.

### How do websites work

- The data we see on websites usually consist of 3 files

-> `HTML (HyperText Markup Language)` 

-> `CSS (Cascading Style Sheets)`

-> `JS (Javascript)`

#### HTML

- Responsibe for the structure of the website

#### CSS

- Responseible for styling the website (how the website looks)

#### Javascript

- Responsible for behaviour of the website (allows the website to do things | functionality)

### HTML Tags

- Looking at one of the most common HTML tags, the heading tags

```HTML
<h1>Hello World!</h1>
```

- Surrounding the content, `Hello World` are the opening and closing tags. The closing tag is denoted by `/` symbol in the brackets `<>`
- `<h1>` opening tag
- `</h1>` closing tag
- `<h1>Hello World</h1>` HTML element


**_Note:_**
- `<h1> -> <h6>`
- Do no have more than 1 h1, you can have more h2's and others but not h1
- Do not skip a heading, go from h1 to h6, using all the heading elements

#### Paragraph element

```HTML
<p>This is a paragraph element</p>
```

- We need paragraph elements to format how the texts are placed on our web page, without `<p>` tag the text will look like this

```HTML
This is a paragraph
This is a paragraph
```

```web
This is a paragraph This is a paragraph
```

- This is with the `<p>` tag, paragraph element

```HTML
<p>This is a paragraph</p>
<p>This is a paragraph</p>
```

```web
This is a paragraph
This is a paragraph
```

#### Void Elements

- Elements that forbid content inside the tags.

```HTML
<hr />
<br />
```
