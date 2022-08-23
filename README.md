# drf_social_network
 
The idea of this project is to create a simple social network backend that lets users create profiles, make friends, and create posts.


Every user has a profile.
Users can send friend requests to each other and accept it.
Users can search for each other by name.
Users can create posts & his friends can see it and make comments & likes.
Users can share images with their stories which last for 24 hours. (only friends)

1)		Account
Register Account with username & password
Change Password
Deactivate Account
		
2)		Profile
Create a profile.
Edit My Profile
Search Profiles

3)		Posts
Create Post
Show Recent Posts for user’s friends (posts feed) with comments & likes count.
Delete, Edit My Post.
Add likes & comments to posts
Show likes & comments for a post

4)   Friends
Send Friend Requests
Accept Friend Requests
Unfriend A Friend
Show My Friends
Mutual Friends

5)  Stories
Create a story
show recent stories for the user’s friends
Each story lasts for 24 hours then it is removed.

		




General Considerations:

1) Each Feature is a Django app
2) All List APIs are paginated.
3) Enable admin panel 
4) Authenticate users using JWT token.
5) SQLite for local development Postgresql for production.
6) Using Docker for deployment.


