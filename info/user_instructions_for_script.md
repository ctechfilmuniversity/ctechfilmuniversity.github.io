# User Instructions for Students

- submission is in a folder, marked with "submission_to_publish_your_last_name"
- submission folder contains minimum a markdown file
    - markdown contains:
        - #Title
        - ##Abstract
        - ##Project Description
        - ##Implementation 
        - ##Lessons learned
- could also contain images
    - please marke one of them a cover by addin the word "cover" to the name

Example for a submission:

```
your folder structure:
.
+-- exercise_1
+-- exercise_2
|   +-- my_cool_project
|       +-- code_files.js
|       +-- ...
|   +-- submission_to_publish_mustermann
|       +-- cool_project.md
|       +-- cover_cool_pixel.gif
|       +-- portrait.jpg
|       +-- systemdiagram.png
|       +-- ... 
```

Example mardown:

    # A Cool Project

    ## Abstract
    This is a cool project.

    ## Project Description.
    It's just here to show you how a submission works.

    ## Implementation
    See above.

    ## Lessons learned
    It teaches you how to do a published submission. I hope you learned something. Fingers crossed. 



# User Instruction for Professors/Lecturers

- clone: [https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io](https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io)
- open [info/local_submission_search.py](https://github.com/ctechfilmuniversity/ctechfilmuniversity.github.io/blob/master/info/local_submission_search.py)

    - replace in lines 13 and 15 the start and destination path

    - the start path is where the script should look for submissions, for instance: ../creative_coding_i/exercises/01
    - **Attention:** Currently is no check for already submitted files available. To avoid redundancy, please create a structure where not all submissions from all exercises are in one folder. Every time you run the programm, you would create a dublicate. Or run the script just once at the end of the semester. 

    - the destination path is where the submission belongs to, for instande: ../ctechfilmuniversity.github.io/_posts/ctech_lectures/creative_coding_i/ws_18_19
    - the destination is somewhere in the _posts folder, the structure of the posts folder is the following:
    ```
    .
    +-- _posts
    |   +-- ctech_lectures
    |       +-- acadamic_methodologies
    |         +-- ss_19
    |         +-- ss_20
    |       +-- creative_coding_i
    |         +-- ws_18_19
    |         +-- ws_19_20
    |       +-- creative_coding_ii
    |         +-- ss_19
    |         +-- ss_20
    |       +-- creative_technologies_i
    |         +-- ws_18_19
    |         +-- ws_19_20
    |       +-- creative_technologies_ii
    |         +-- ss_19
    |         +-- ss_20
    |       +-- orientation_project
    |         +-- ss_19
    |         +-- ws_18_19
    |         +-- ss_20
    |       +-- procedural_generation_and_simulation
    |         +-- ss_19
    |         +-- ss_20
    |       +-- theoretical_backgrounds_for_audio_and_graphics
    |         +-- ws_18_19
    |         +-- ws_19_20
    |   +-- individual_projects
    |       +-- electives
    |         +-- ws_19_20    
    |   +-- master_theses
    |       +-- ws_18_19
    |       +-- ss_20
    ```
    - run the script
    - commit the changes 
    - push the changes

    For questions text me: Franziska.Paetzold@filmuniversitaet.de