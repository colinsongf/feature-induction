# feature-induction

**under construction**

Here we investigate algorithms to perform feature induction for text classification. In particular, we are interested in examples like:

> I do not like this movie.

Sentiment classification has trouble with this because of negation. This is a problem both at training time (since "like" will be encouraged to have a somewhat negative weight) as well as at testing time (since "like", if positive, will encourage a positive classification).

Our idea is to selectively increase the complexity of certain features. For example, this sentence would be represented with a feature "not like" instead of "like." The challenge is to generalize this for other examples.
