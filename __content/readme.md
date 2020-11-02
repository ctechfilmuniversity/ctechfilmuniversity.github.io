# How to create a new post
## 1 Write post
In order to write your post, use the following MarkDown template. Name the file after your project title, e.g. "example-project.md".

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

### 1.1 Filling in the meta information
As stated in the comments in the header section, please replace all occurances of "xxxx" with your information on the project. Please add as many tags, as you like. You can look for tags on the [website](https://ctechfilmuniversity.github.io/).

### 1.2 Writing the actual content
Please keep the given headings for your post, since it will give all posts a more coherent structure. But you are free to add additional sub headings, if you want to. 

#### 1.2.1 Images
Images can be added according to MarkDown syntax, but you have to keep the image files in the same folder, as your Markdown post. Always use a relative path to your pictures, in particular just provide the file name, e.g.:
```
![very-nice-picture](myPicture.png)
```


### 1.2.2 Videos
You can embed videos from Youtube or Vimeo. Just use the code fragments below and fill in the video id between the two quotation marks behind "id". Please keep in mind, that you have to use the video id, not the url. You can find more information on that in the following descriptions for YouTube and Vimeo.

**Youtube:**

You can find the video id in the url after "watch?v=". In the following url example, the id is highlighted: [https://www.youtube.com/watch?v=**YRt1j9MHTZU**](https://www.youtube.com/watch?v=YRt1j9MHTZU) 
```
{% include youtube.html id="" %}
```

**Vimeo:**

You can find the video id in the url after the last slash. In the following url example, the id is highlighted: [https://vimeo.com/**6919518**](https://vimeo.com/6919518) 
```
{% include vimeo.html id="" %}
```


### 1.3 Example
You can always have a look, at preexisting posts, that can be found in this folder ("__content"). Every post has its own folder, beginning with the date.

Furthermore here is a made up example:
```
---
layout: post
title: "Example Project"
author: "Max Muster"
categories: Projects
tags: WS1819 OrientationProject PhysicalComputing Audio

cover-image: very-nice-project-banner.jpg
cover-image-title: Project Key Visual
---

## Abstract
This is my project "Example Project", which has been...

## Project description
My intention on this project was to...

### Media
Here you can see...
![very-nice-picture](myPicture.png)

## Implementation
To implement my idea, several technologies and...

## Lessons learned
Time was the most limiting factor...

```

## 2 Create the post on the website
### 2.1 Checkout the repository and create a branch
Checkout the following repository:
```
https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io.git
```
Create and checkout a branch for your project locally, you can name the branch for example after your project.

### 2.2 Commit and push the post files
Copy your files to the folder "__content/new-post/". All files should be in the same folder level, do not create sub directories. Commit and push the files. Your files should contain:
* One Markdown file with the textual content, based on the provided template
* Image files

### 2.3 Create a pull request
Visit the following URL with a webbrowser: https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io/compare

Click on "New pull request". Select for base "master" and for compare your branch. Click on "Create pull request". Select a Reviewer, for example Phil Clausen or Markus Traber. Click on "Create Pull Request". Wait for the reviewer to merge your branch into master.

### 2.3 Post published
After the branch has been merged, Github will automatically process the post. Wait for a new commit by "GitHub Action" titled "Automated content creation push" to be pushed to the repository. This should normally take place within a minute, maybe a little more.

After some more minutes, the post should also be published on the live website.

## 3 Modifying existing posts
Please keep in mind, that you always have to pull in order to get newest repository state. You also have to always create a branch and follow the previously mentioned steps of creating a pull request and merging the content. 

### 3.1 Editing posts
In the folder "__content" all posts are kept in separate folders, beginning with the publishing date, followed by its project name, e.g. "2020-03-23-example-project".

Files within that folder can be edited, commited and pushed. Github will automatically publish the changes after a few minutes, when your pull request has been approved and merged. 

### 3.2 Deleting posts
In order to delete a post, files in three different folders have to be deleted:
* The complete folder in "__content/", e.g. "2020-03-23-example-project"
* The MarkDown file of the project in "_posts/projects/", e.g. "2020-03-23-example-project.md"
* The complete assets folder of the project in "assets/img/projects/", e.g. "2020-03-23-example-project"
