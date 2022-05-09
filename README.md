# README

Following [Shinichi Okada's tutorial on levelup.gitconnected](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864)

## Notes

### Helpers function to open file

At the stage where we import all the helpers function from library I had to clean that up a bit by filling in app/library/__init__.py like this:

```python

from .helpers import openfile

__all__ = ["openfile"]
```


### Updating page.html after adding openfile

When we update page.html there wasn't instructions on what parts to replace, I had luck with replacing:

```html
<h1>
WElcome to FastAPI Starter.
</h1>

{{data.page}}
```

with...

```html

<main role="main" class="container">
    <div class="row">
        <div class="col">
            {{data.text|safe}}
        </div>
    </div>
</main><!-- /.container -->
```


### Adding active class to unsplash

The tutorial Makes it very unclear where to add `{% set active_page = "unsplash" %}` because the html that's shows in the gist is definitely not right...

I made the change by just adding that one line underneath `{% extends "base.html" %}`

### Adding Two Forms

The tutorial has us add html to the twoforms.html and accordian.html before doing anything in python files and shows a working site in the sample video.
However, Just adding to the html didn't give me nice pages I _guess_ because there's nothing in the relevant python files?

I just fine the ordering of this tutorial really confusing... not well-laid out for a linear flow
