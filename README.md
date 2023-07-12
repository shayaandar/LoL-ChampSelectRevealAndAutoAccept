# Queue Assist

Queue Assist is a League of Legends auto queue acceptor and champ select team reveal tool.  

This script utilizes the League of Legends LCU (League Client Update) API to automate the acceptance of ready checks during queue as well as auto start queues. Additionally, it pulls up teammate stats on u.gg for quick reference during champion selection.

## How to Use

1. Clone the repository to your local machine.
2. Make sure your League of Legends client is open.
3. Run the provided GUI script.
4. Toggle the button to enable the script.
5. Queue up for a game.

Once the script is toggled on, it will automatically start your queue if you are in a lobby. For ranked lobbies, you must input your position preference first. After matchmaking starts, it will accept all ready checks that appear during champion select. Then, following a short delay, it will open u.gg multisearch to display the stats of your teammates for quick reference.

## UPDATES 
v1.1 
- Checkboxes have been added for auto queue acceptance and champ select reveal so the user can elect to have one or the other if not both
- Cosmetic GUI updates
- Auto matchmaking start functionality was added - once user makes a lobby script will automatically start searching for a match

v1.2 
- Fixed issues with checkboxes not operating properly
- Added executable functionality - still requires user testing

## Future Additions
Enhanced GUI and Customization: Enhance the graphical user interface (GUI) to offer a more intuitive and user-friendly experience. Consider incorporating additional options and settings for customization based on user preferences.

Auto Play Again/Requeue: Extend the script to include an auto play again or requeue feature. This enhancement would enable users to automatically queue up for another game once the current one ends. It simplifies the gameplay experience by eliminating the need for manual interaction between matches.


Feel free to explore and customize the script further to meet your specific needs and preferences. Any feedback, contributions, and improvements are welcome.
