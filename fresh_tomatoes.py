import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<title>My Movies</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3-theme-blue.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css">
<script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<style>
    #trailer-video{
        width:100%;
        height:500px;
    }
</style>
<script type="text/javascript">
        function open_modal(){
            document.getElementById('id01').style.display='block'
            // Start playing the video whenever the trailer modal is opened
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        }
        function close_modal(){
            document.getElementById('id01').style.display='none'
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        }
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
</script>
'''


# The main page layout and title bar
main_page_content = '''
   <body>
    <!-- Main Page Content -->
    <div class="w3-row w3-padding-8 w3-theme-d2 w3-xlarge">
      <div class="w3-quarter">
        <ul class="w3-navbar">
          <li><a href="#"><i class="fa fa-bars"></i></a></li>
        </ul>
      </div>

      <div class="w3-half">
        <input type="text" class="w3-blue w3-border-0 w3-padding" style="width:100%">
      </div>

      <div class="w3-quarter">
        <ul class="w3-navbar">
          <li class="w3-left"><a href="#"><i class="fa fa-search"></i></a></li>
          <li class="w3-navitem w3-right w3-hide-small"><img class="w3-circle" src="img_avtar.jpg" style="height:35px;"></li>
        </ul>
      </div>
    </div>

    <div class="w3-container w3-padding-32 w3-theme-d1">
      <h1>Lis of My Favourite Movies</h1>
    </div>

    <div class="w3-row-padding" style="width:1000px; cusor:pointer">
       {movie_tiles}
    </div>

    <div class="w3-container w3-theme-d2">
        <p class="w3-large">My movies 2016</p>
    </div>

     <!-- Trailer Video Modal -->
        <div id="id01" class="w3-modal modal" id="trailer">
            <div class="w3-modal-content modal-content">
                <span class="w3-closebtn" onclick="close_modal()">&times;</span>
                <div class="scale-media" id="trailer-video-container"></div>
            </div>
        </div>
</body>
'''


# A single movie entry html template
movie_tile_content = '''
    <div class="w3-third w3-section"  onclick="open_modal()" data-trailer-youtube-id="qas5lWp7_R0">
            <div class="w3-card-4">
                <img src="{cover_url}" width=100% height="200">
                <div class="w3-container w3-white">
                    <h3><b>{movie_title}</b></h3>
                    <p>{story_line}</p>
                </div>
            </div>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            cover_url=movie.cover_url,
            story_line = movie.storyline,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
