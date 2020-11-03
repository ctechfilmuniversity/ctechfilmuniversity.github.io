# How to create a new post
## 1 Write post
In order to write your post, use the following MarkDown template. Name the file after your project title, e.g. `example-project.md`.

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
As stated in the comments in the header section, please replace all occurances of `xxxx` with your information on the project. Please add as many tags, as you like. You can look for tags on the [website](https://ctechfilmuniversity.github.io/). Please be sure to include the current semester in an abbreviated form like the following examples: `WS1920`, `SS20`, `WS2021`. Furthermore include an abbreviated form of the subject you created the project for, e.g.: `PGS`, `CC1`, `CC2`, `TBAG`, `TI`, `OrientationProject`.

### 1.2 Writing the actual content
Please keep the given headings for your post, since it will give all posts a more coherent structure. But you are free to add additional sub headings, if you want to. 

#### 1.2.1 Images
Images can be added according to MarkDown syntax, but you have to keep the image files in the same folder, as your Markdown post. Always use a relative path to your pictures, in particular just provide the file name, e.g.:
```
![very-nice-picture](myPicture.png)
```


### 1.2.2 Videos
You can embed videos from Youtube or Vimeo. Just use the code fragments below and fill in the video id between the two quotation marks behind `id`. Please keep in mind, that you have to use the video id, not the url. You can find more information on that in the following descriptions for YouTube and Vimeo.

**Youtube:**

You can find the video id in the url after `watch?v=`. In the following url example, the id is highlighted: [https://www.youtube.com/watch?v=**YRt1j9MHTZU**](https://www.youtube.com/watch?v=YRt1j9MHTZU) 
```
{% include youtube.html id="" %}
```

**Vimeo:**

You can find the video id in the url after the last slash. In the following url example, the id is highlighted: [https://vimeo.com/**6919518**](https://vimeo.com/6919518) 
```
{% include vimeo.html id="" %}
```


### 1.3 Example
You can always have a look, at preexisting posts, that can be found in the folder `__content`. Every post has its own folder, beginning with the date.

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
Open the terminal app or the equivalent on your operating system and change the directory to the folder, where you want to download the contents of this repository to.

Linux / MacOs:
```
// absolute path
cd /path/to/the/folder

// relative path to the current path in your terminal
cd relative/path/to/the/folder

// absolute example on MacOs
cd /Users/max/Coding/Ctech

// relative example on MacOs (normally the terminal starts out in your users directory)
cd Coding/Ctech
```

Windows:
```
// you might need to switch first to a different disk, 
// if so you can do so by just writing the the drive letter, 
// like the following example with the drive letter "C".
C:

// absolute path
cd C:\path\to\the\folder

// relative path
cd relative\path\to\the\folder

// absolute example
cd C:\Users\max\Coding\Ctech

// relative example (normally the command prompt starts out in your users directory)
cd Coding\Ctech
```
If you have difficulties using `cd`, just do a quick research online, there are plenty resources regarding how to use it on your operating system.

Now checkout this repository:
```
git clone https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io.git
```

Create a local branch, you can name it after your project:
```
git branch yourAwesomeProjectBranch
```

Checkout your branch:
```
git checkout yourAwesomeProjectBranch
```

### 2.2 Commit and push the post files
Copy your files to the folder `__content/new-post/`. All files should be in the same folder level, do not create sub directories. The folder should contain:
* One `readme.md`, which has already been, there and should not be touched!
* One Markdown file with the textual content, based on the provided template
* Image files

Add your newly added files to git index:
```
git add --all
```

Commit and append a message, that is a reference to your project:
```
git commit -a -m "Adding my project SuperAwesomeProject"
```

Push the changes and your Branch to the remote Repository (GitHub):
```
git push --set-upstream origin yourAwesomeProjectBranch
```

### 2.3 Create a pull request
Replace the last part of the URL with your branch name and open the URL with a web browser: https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io/pull/new/yourAwesomeProjectBranch

Click on `Create pull request`. 

Wait for a reviewer to merge your branch into master. If you want to accellerate the process, write a mail to Phil Clausen or Markus Traber.

### 2.3 Post published
After the branch has been merged, Github will automatically process the post. Wait for a new commit by "philclausen" titled "Automated content creation push" to be pushed to the repository. This should normally take place within a minute, maybe a little more.

After some more minutes, the post should also be published on the website.

## 3 Modifying existing posts
The whole process of changing posts is basically the same as the steps explained in section 2. You create a local branch, make changes, commit and push the changes to the remote repository and create a pull request. Please try to keep your local repo always up-to-date, like described in 3.1.


## 3.1 Updating the local repository
You should always pull the newest changes to this repository, before editing stuff.

Check that you are on the `master` branch:
```
git checkout master
```

Pull the lastest changes:
```
git pull
```

Create a branch, like mentioned in step 2.1.

### 3.2 Editing posts
In the folder "__content" all posts are kept in separate folders, beginning with the publishing date, followed by its project name, e.g. "2020-03-23-example-project".

Make changes to these files in order to change already public posts.

### 3.3 Deleting posts
In order to delete a post, files in three different folders have to be deleted:
* The complete project post folder inside `__content/`, e.g. `2020-03-23-example-project`
* The MarkDown file of the project in `_posts/projects/`, e.g. `2020-03-23-example-project.md`
* The complete assets folder of the project inside `assets/img/projects/`, e.g. `2020-03-23-example-project`
