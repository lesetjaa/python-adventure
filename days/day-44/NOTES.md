# Notes

## CSS properties

- Here is how we can set basic colors to our html

```CSS
html {
    background-color: blue;
}

h1 {
    color: black;
}
```

- `html` / `h1` - html element
- `background-color` - property
- `blue` / `black` - value

### CSS colors

- using colors with their names are from css values called css named colors

#### Hex Code Colors

- hex codes are a they represent a larger number code for that particular color

```CSS
h1 {
    color: #DAB716
}
```

## Font Properties

```CSS
h1 {
    color: blue;
    font-size: 20px
    font-weight: bold;
    font-family: sans-serif;
}
```

#### Font size

```CSS
h1 {
    font-size: 20px
}
```

- `font-size` this changes big or small (size) of the text should be

##### ways of representing font-size ([-explanation-](./style.css))

- `pixels` (px) - 1/96th inch
- `point` (pt) - 1/72nd inch
- `em` (em) - it takes the size of the parent's font size (1em = 100% of the parent)
- `rem` (rem) - it takes the size of the root's font size (2rem = 200% of the root) (recommended)

#### Font weight

```CSS
h1 {
    font-weight: bold;
}
```

- `font-weight` this changes thickness or boldness of the text should be

##### ways of representing font-weight ([-explanation-](./style.css))

- `keywords` (normal/ bold) - comes with css
- `relative to parent` (lighter/ bolder) - it uses the parent's text weight to determine its own
- `number` (100-900) - how lighter or bolder the text should be

#### Font family

```CSS
h1 {
    font-family: helvetica, sans-serif;
}
```

- `font-family` this changes how the font looks like

##### ways of representing font-family ([-explanation-](./style.css))

- `keywords` (helvetica/ sans-serif) - these are typefaces, we usually have more than one value (add generic) because some browsers dont have certain typefaces/ fonts
- `many worded fonts` ("Times New Roman") - use quotations

**_Note:_** `sans-serif`, corners of characters are right angle and `serif` are not

##### Custom fonts ([-explanation-](./index.html))

```HTML
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&family=Outfit:wght@100..900&family=Shantell+Sans:ital,wght@0,300..800;1,300..800&display=swap"
        rel="stylesheet">

    <style>
    h1 {
        font-family: "Shantell Sans", cursive;
    }
    </style>
```

- Link the custom font in the html file and we can reference it when we style our page, using quotations (shown above)

#### Text Align

```CSS
h1 {
    text-align: center
}
```

- `text-align` this changes the text alignment, it is where the text is placed (center, left, right)
- Text alignment ([-implementation-](./style.css))

### CSS Inspection (Developer Tools)

- In chrome on a website, we can access it in the settings or shortcut `⌥⌘I` -> (Option + Command + I) or right click an element and choose the `inspect` option
  OR we can select an element visually using a pointer at the top left of the developer tools window

### The Box Model

- The Margin, Padding and Border properties form the box model concept

#### The Box model

- This means we should think of each and every element as a box

```CSS
height: 600px
width: 600px
```

- we can use pixels to set the width of an element or we can also use percentages

#### CSS Border

```CSS
border: 10px solid black
```

- It accepts 3 values, thickness, style and color of the border

- `10px` - thickness of the border
- `solid/ dashed` - style of the border
- `black` - color of the border

````

```CSS
border: 30px solid red
border-top: 0px
````

- we can choose which side of the border to style with properties like `border-top`

**_Note_** This has to be defined after the border has been set

```CSS
border-width: 0px 10px 5px 20px
```

- we can change the border width of each side individually by defining it separetly.
- It is defined from the top in a clockwise direction, so its -> **border-width: top right bottom left**
- In addition, we can provide two values which will set top and bottom together then lfet and right together -> **border-with: top-bottom sides**

#### Padding

```CSS
h1 {
    padding: 20px;
}
```

- This sets the space between the border and the content in the border

#### Margin

```CSS
.container {
    margin: 5px;
}
```

- This sets the space between the border and the outside of the border

**_Note:_** The `Marign`, `Padding` and `Border` properties are defined the same way as css border was [explained](#css-border)

### Creatig our own elements

```HTML
<div>
    <p>Hello World</p>
    <img src="./image.png" />
</div>
<div>
    <p>Good Night</p>
    <img src="./image2.png" />
</div>
```
- We can use the `div` element to create our own boxes to wrap content of the same topic seperate from other content
