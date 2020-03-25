# How to create a new post
## Write post
In order to write your post, use the MarkDown template, provided here: [Post Template](template_post.md)

You can also copy it from below:

```
---
# Please replace every occurrence of "xxxx" in this header area with your personal information.
layout: post
title: "xxxx"
author: "xxxx"
categories: Projects
tags: xxxx xxxx xxxx # please add suitable tags — separated by a space — the number of tags is not limited

# The cover image will be seen first. It will also be used to enlist your project amonst others.
cover-image: xxxx.jpg # choose your desired image file format — must be supported by web browsers — only one
cover-image-title: xxxx # a descriptive title for the image
---

## Abstract

## Project description

## Implementation

## Lessons learned
```

### Filling in the meta information
As stated in the comments in the header section, please replace all occurances of "xxxx" with your information on the project. Please add as many tags, as you like. You can look for tags on the [website](https://ctechfilmuniversity.github.io/).

### Writing the actual content
Please keep the given headings for your post, since it will give all posts a more coherent structure. But you are free to add additional sub headings, if you want to. 

#### Images
Images can be added according to MarkDown syntax, but you have to keep the image files in the same folder, as your Markdown post. Always use a relative path to your pictures, in particular just provide the file name, e.g.:
```
![very-nice-picture](myPicture.png)
```

### Example
You can always have a look, at preexisting posts, that can be found in this folder. Every post has its own folder, beginning with the date.

Furthermore here is a made up example:
```
---
layout: post
title: "My very nice project"
author: "Max Muster"
categories: Projects
tags: WS1819 OrientationProject PhysicalComputing Audio

cover-image: very-nice-project-banner.jpg
cover-image-title: Project Key Visual
---

## Abstract
This is my project "My very nice project", which has been...

## Project description
My intention on this project was to...

### Media
Here you can see...

## Implementation
To implement my idea, several technologies and...

## Lessons learned
Time was the most limiting factor...

```

