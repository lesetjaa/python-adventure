# Notes

## HTML Structure

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Website Title</title>
    </head>
    <body>
        <h1>The content goes here</h1>
    </body>
</html>
```

- `<!DOCTYPE>` declaration tells HTML which version the html was written in, the latest version is HTML5
- `<html lang="en">` this is the root element, everything goes in these tags, `lang` tells the language of the content
- `<head>` this is where the important information about our website goes, this will not be shown to the user.
- `<meta>` `charset="UTF-8`this ensures the characters that are used in the HTML file to render, other character sets do not allow emojis to render.
- `<title>` This gets displayed in the tab bar in the browser. This will be the title of the page

- `<body>` This is where all the content of the website goes between, images, text, lots of things

## List Elements

### Unordered List

```HTML
<ul>
    <li>Milk</li>
    <li>Eggs</li>
    <li>Flour</li>
</ul>
```

- `<ul>` This is the enclosure of our list and it also determines what type of list it is
- `[ordered list]` Bulleted list
- `<li>` [list item] These are list items, they contain some piece of content

#### How it will look

```Web
• Milk
• Eggs
• Flour
```

### Ordered List

```HTML
<ol>
    <li>Milk</li>
    <li>Eggs</li>
    <li>Flour</li>
</ol>
```

- `[ordered list]` Numbered list

#### How it will look

```Web
1. Milk
2. Eggs
3. Flour
```

### Anchor elements: HTML attributes

```HTML
<a>This is a link</a>
```

- This is an anchor element
- We have attributes in HTML that go in the opening tag of an element (just after the name of the tag)
- `attribues` adds additional information to the elements

Here is how it is structured

```HTML
<tag attribute=value>Content</tag>
```

- `tag` - name of the HTML element
- `attribute` - name of the attribute
- `value` - value of the attribute

**_Note:_** These are separated by the space character

- `href` - this attribute contains what the hyperlink should go to

### Image element

```HTML
<!-- self closed tag (void element) -->
<img src="url" />
```

- `src` - source fof the image
- `url` - location of the image
- `alt` - alternative text description
