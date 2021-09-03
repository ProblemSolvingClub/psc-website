# Website for the Competitive Programming Club 

Built using HTML, CSS, Javascript, and Bootstrap. Statically generated and tested with Jekyll. 

## Local development 
You can test the website on both your local computer and mobile device.

### Installing Jekyll
1. Install Jekyll based on [the type of command line you are using](https://jekyllrb.com/docs/installation/)

### Computer setup (computer viewing only)
1. Run `jekyll build` to process the website into `_site`
2. Run `jekyll serve` to host the site on [localhost:4000](http://localhost:4000)

### Mobile device setup (computer and mobile device viewing)
1. Make sure your local machine and mobile device are connected to the same WiFi network
2. `jekyll build` on the computer
3. Then, run `jekyll serve --host=0.0.0.0`
4. Find the private IP address of the computer you're hosting the site on by running `hostname -I`
5. Enter web address `yourPrivateIP:4000` on your mobile device browser. Computer web address will still be at `localhost:4000`

### Example links
Test these links to see whether you have successfully hosted the website on your local machine:
- [Home](http://localhost:4000)
- [About](http://localhost:4000/about)
- [Contests > ACPC > 2015](http://localhost:4000/contests/acpc/2015)

### Using CPanel
1. Once you have completed making all the changes to the website, merge your branch into master
2. Go to this link to access [CPanel](cpc2.cpsc.ucalgary.ca/cpanel)
    ```
        username: cpc
        password: *ask an admin*
    ```
3. Navigate to `File Manager` -> `public_html`
    - This directory is where you will be uploading your `_site` contents
    - You won't be able to upload folders in the directory so to work around this follow these steps:
        1. zip the contents of the `_site` folder
        2. upload the zipped file to CPanel in the `public_html` directory
        3. Extract the zipped file in CPanel
        4. Ensure that all files from `_site` is in the `public_html` directory
4. Now, to update the latest changes from the repo, navigate to `Git Version Control`
    - Click on manage then the `Pull or Deploy` tab
5. Simply click on `Update from Remote` then `Deploy HEAD Commit` last
6. That's it! Now just test the website if the changes worked

## Branch naming conventions

#### Bugs
- bug/[short description of bug]

#### Blog post
- post/[title of blog post]

#### Enhancement 
- enhancement/[short description of enhancement]

## Updating the website
Any time the website needs to be updated (whether it's a post, enhancement, bug, etc.), commits should all be pushed to a new branch and then merged to master through a pull request. Do **not** push commits directly to master.

1. Checkout to master and update your local file repository with its contents.

    - `git checkout master`
    - `git pull`

2. Create a local branch for the change you are making based on the branch naming conventions listed above. For example, if I were to make a post announcing ACPC 2025 I would name it `post/acpc-2025`

    - `git branch localBranch`
    - `git checkout localBranch`
    - `git push -u origin localBranch`

3. Push commits to local branch and create a pull request to master. 

4. Assign another VP technology executive (or someone who knows how this repository works) to review and approve your commits before merging to master. 

5. After confirming the validity of the live site, delete the branch you were working on.

## Making a blog/main page post 

The .md file will differ on variables and styling based on the post type. 

#### Contest announcement post
- `title` (required): The title of the blog post
- `contestPoster` (required): The directory path to the contest image
- `infoBtnLink` (required): The link to the contest page on our website
- `signupBtnLink` (required): The external sign-up link for the contest
- `text` (required): The contest post text, except without the html/css styling

#### Regular post (everything else)
- `title` (required): The title of the blog post
- `img1` (optional): The image associated with the post. If you require additional images, add `img2`, `img3`, etc.
- `text` (required): The contest post text, except without the html/css styling
