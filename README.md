# Website for the Problem Solving Club

## Local development setup
1. Install jekyll via `gem install jekyll`
2. Run `jekyll build` to process the website into `_site`
3. Run `jekyll serve` to host the site on [localhost:4000](http://localhost:4000)

### Example links
- [Home](http://localhost:4000)
- [About](http://localhost:4000/about)
- [Contests > ACPC > 2015](http://localhost:4000/contests/acpc/2015)

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

4. Assign another VP technology executive to review and approve your commits before merging to master. 

## Making a blog/main page post 

The .md filet will need differ on variables and style based on the post type. 

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









