# HASOC
german_convert.py and hinglish_convert.py are the script files used to prepare dataset.
The dataset differs in that the determination of whether a comment or a reply falls under the category of hate speech depends on both the main tweet and the comment in the case of a reply. For instance, a comment of "yes" is meaningless by itself, but if it is made in response to a main tweet that is hate speech, then it considers as hate speech, while a comment of "no" for the same tweet does not. Therefore, the modification we made to get it ready for the model (to capture the context of the tweet, comment, and reply) is that the text for the main tweet remains the same, the main tweet is appended to the comment, and the main tweet and as well as the comment is appended to the reply text(separated by blank space). This way, it will be able to capture the context of the comment and reply.

  Main tweet: <main tweet>
  Comment: <main tweet> <comment>
  Reply: <main tweet> <comment> <reply>
