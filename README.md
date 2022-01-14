# Pylitics

This is a python programm that attempts to give tools to model the political spectrum.


This library is just setting some bones for doing this kind of political
modelling.
Feel free to use it and suggest any change.

## Implementation

It considers the political space to be a set of variable where
every one resides at one spot on the diagram.


The variables go from 0 to 1, where 0.5 means the person is indiferent,
0 if the person is againts and 1 if the person is in favor.

The same is applied for how important a subject is to a point.

We use np.nan to represent missing values.




Start quote:
 In spatial
models of party or candidate competition, policies or platforms are represented geometrically
as points in a k-dimensional Euclidean space, k ∈ N, the ‘political space’.
Its dimensions
correspond to the different issues the electorate consider important. Each voter is assumed to
have a most preferred policy or ideal point within this space. A voter’s utility for a policy
declines with the distance of the policy from his or her ideal point
See https://repub.eur.nl/pub/111247