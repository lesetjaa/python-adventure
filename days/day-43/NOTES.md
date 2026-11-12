# Notes

## CSS - Cascading Style Sheets

- `Cascade` - The way in which we apply style is like a waterfall that is why it is called cascade style sheet
- We start from the most general

`Style Sheets` - language that allows us to specify how our website looks. example: `sass`; `less`

### Why we need css

- HTML does not allow us to control how our documents (HTML documents) look like, they had no variation

### How to add CSS

- We have 3 ways we can add css into our HTML `inline`, `internal` and `external`

#### Inline

```HTML
<html style="background: blue">
</html>
```

- It goes into the same line as the HTML element you want to style
- use the `style` attribute to
- These are useful when we are just adding a single style to an element in HTML

#### Internal

```HTML
<html>
    <head>
        <style>
            /*  selector  */
            html {
                background: blue;
            }
        </style>
    </head>
</html>
```

- this `style` element can be added anywhere in our html document
- In this element we use selectors to choose which element to style
- The CSS goes into the curly braces after the selector
- These are useful when we are just applying it to one HTML document

#### External

```HTML
<html>
    <head>
        <link rel="stylesheet"
        href="./style.css"
        />
    </head>
</html>
```

```CSS
/* style.css file */
html {
    background: blue;
}
```

- The syles live in a completely different file
- To link the style to the HTML we use the `link` element, and add these two attributes
- `rel` - Relationship of the file to the HTML document
- `href` - Location of the file

### CSS selectors

```CSS
color: blue
```

- `color` - property we want to change
- `blue` - value we want to change to

#### CSS selector

- The part that selects the HTML that the rules are applied to

```CSS
h1 {
    color: blue
}
```

- `h1` - This is the selector, it targeting all h1 elements

##### Class Selector

```CSS
.read-heading {
    color: red
}
```

- This required a `dot` and the name of the `class`
- `red-heading` - The name of the class

**_Note:_** a A class is an attribute that can be added to any html element, it is used to group elements

```HTML
<h2 class="read-heading">Red</h2>
```

##### Id Selector

```CSS
#main {
    color: red
}
```

- This required a `pound sign` and the name of the `id`
- `main` - The name of the id

**_Note:_** a A id is also an attribute that can be added to any html element, it should only be applied to one element in a single HTML file

```HTML
<h2 id="main">Red</h2>
```

##### Attribute Selector

```CSS
p[draggable] {
    color: orange;
}
```

- It starts with an html element, then the attribute in squared brackets

```CSS
p[draggable="false"] {
    color: purple;
}
```

- we can also choose by attribute with a specifc value we want

```HTML
<p draggable="true">Drag me</p>
<p draggable="false">Don't Drag me</p>
<p draggable="false">Don't Drag me</p>
```

- all the `draggable="false"` paragraph elements will be purple

##### Universal Selector

```CSS
* {
    color: green;
}
```

- This selects all the elements in the HTML document, it applys to everything
