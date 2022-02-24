# Website for the Competitive Programming Club 

Built using HTML, CSS, Javascript, and Bootstrap. Statically generated and tested with Jekyll. 

## How it all works

* Already know? Skip to the [TODO LIST](#todo-list)!
* Need a reminder on how to update the site? [click here](#making-changes)

[Jekyll](https://jekyllrb.com) is a static site generator.
The majority of this repo's structure is relevant to how jekyll works.

When you run `jekyll serve` any changes you make (when saved) will automatically be compiled and displayed.
If this does not happen run `jekyll serve --watch`.
Calling `jekyll build` generates a `_site` directory which will contains all the static site information.

When it comes time to loading your changes on to the live site you need to go through cPanel

## Local development 
You can test the website on both your local computer and mobile device.

### Installing Jekyll
1. Install Jekyll based on [the type of command line you are using](https://jekyllrb.com/docs/installation/) 
 
    *NOTE:* GCC is a huge pain in the ass to install on a windows operation system.
    use this incredibly shady link to install it much easier: (https://sourceforge.net/projects/mingw-w64/)
2. Run gem install jekyll-paginate

3. If using Ruby 3.0 or later, make sure to install webrick with `gem install webrick`

### Computer setup (computer viewing only)
1. Run `jekyll build` to process the website into `_site`
2. Run `jekyll serve` to host the site on [localhost:4000](http://localhost:4000)

### Mobile device setup (computer and mobile device viewing)
1. Make sure your local machine and mobile device are connected to the same WiFi network
2. `jekyll build` on the computer
3. Then, run `jekyll serve --host=0.0.0.0`
4. Find the private IP address of the computer you're hosting the site on by running `hostname -I`
5. Enter web address `yourPrivateIP:4000` on your mobile device browser. Computer web address will still be at `localhost:4000`

*The information above may be out of date and has not been verified as of February 23, 2022.*

## Making Changes

To make changes here are some tips:

### Blog Posts

1. To make a new blog post go to [`_posts`](_posts/). You can copy paste the previous post.
    - The name should be `<year>-<month>-<day>-<Name>.md`. It will not work otherwise.
    - The yaml front matter (stuff at the top inside those `---`) will be displayed inside of the home page. This metadata includes:
        - `title` (required)
            - The title of the blog post
        - `contestPoster` (required)
            - The directory path to the contest image
            - This will display the same image in both the home and blog post.
        - `infoBtnLink` (required):
            - A link for more information.
            - For contests this should be the link to the actual contest's page on the ccpc website.
        - `signupBtnLink` (required)
            - A link to signup to the event. (For contests it is usually the same eventbrite link).
        - `text` (required)
            * This is the text that shows up on the home page, it is different from the text that shows up in the blog post.
    - The rest of the HTML you write will be displayed like the rest of the [blogs](https://cpc2.cpsc.ucalgary.ca/blog/).
        - You really do not need to do anything fancy here, just do not create or delete any divs and make a few paragraphs with some **bold** or *italic* text here and there.

### Images

2. Images go into the `/img/` drectory.

### Contest Information

3. When a new contest is announced go into [`contests`](contests/) and into the appropriate directory (or make one).
    - Just copy paste the previous year's announcement.
    - Make sure to change the poster inside the `img` tag (`id` should be `header`).
    - The HTML is pretty striaghtforward if you know HTML, just make the necessary changes when they are needed.

## Using CPanel
1. Once you have completed making all the changes to the website, merge your branch into master
2. Go to this link to access [CPanel](cpc2.cpsc.ucalgary.ca/cpanel)
    ```
        username: cpc
        password: *saved to LastPass*
    ```
3. Now, to update the latest changes from the repo, navigate to `Git Version Control`
    - Click on manage then the `Pull or Deploy` tab
4. Simply click on `Update from Remote` then `Deploy HEAD Commit` last
5. Navigate to `File Manager` -> `public_html`
    - This directory is where you will be uploading your `_site` contents
    - First delete everything in within the `public_html` directory and then process with the steps
    - You won't be able to upload folders in the directory so to work around this follow these steps:
        1. zip the contents of the `_site` folder
        2. upload the zipped file to CPanel in the `public_html` directory
        3. Extract the zipped file in CPanel
        4. Ensure that all files from `_site` is in the `public_html` directory (this may require some copy pasting)
6. Then hopefully that's it! Now just test the website with an Incognito browser and check to see if the changes worked
7. If you don't see changes in your regular browser you just might need to clear your cookies on the site

### Example links
Test these links to see whether you have successfully hosted the website on your local machine:
- [Home](http://localhost:4000)
- [About](http://localhost:4000/about)
- [Contests > ACPC > 2015](http://localhost:4000/contests/acpc/2015)

[Back to top](#website-for-the-competitive-programming-club)

# Possibly Outdated but Useful

## Branch naming conventions

#### Bugs
- bug/[short description of bug]

#### Blog post
- post/[title of blog post]

#### Enhancement 
- enhancement/[short description of enhancement]

#### Update
- update/[short description of update]

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

# TODO LIST:

- [ ] Get RSA keys for server
- [x] CCPC 2022 contest post
- [x] Advertisement for Resume Event
- [x] Update [roster](about/)
- [ ] Fix leaderboard
- [ ] Redirect [https://cpc.cpsc.ucalgary.ca/ccpc](https://cpc.cpsc.ucalgary.ca/ccpc) to the ccpc 2022 page
- [ ] Move away from CPanel (our server??)
- [ ] Update prize draw

[Back to top](#website-for-the-competitive-programming-club)
