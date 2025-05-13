
% actions

% go
act( go(X,Y),                                           % name
     [in(shakey,X), on(shakey,floor), connected(X,Y)],  % preconditions
     [in(shakey,X)],                                    % delete
     [in(shakey,Y)]                                     % add
     ).

% push
act( push(B,X,Y),                                                                                         % name
     [in(shakey,X), on(shakey, floor), box(B), in(B,X), connected(X,Y), lightOn(X)], % preconditions
     [in(shakey,X), in(B,X)],                                                                             % delete
     [in(shakey,Y), in(B,Y)]                                                                              % add
     ).

% climbUp
act( climbUp(B),                                         % name
     [box(B), in(shakey,X),on(shakey,floor), in(B,X)],   % preconditions
     [on(shakey,floor)],                                 % delete
     [on(shakey,B)]                                      % add
     ).

% climbDown
act( climbDown(B),                                   % name
     [box(B), in(shakey,X),on(shakey,B), in(B,X)],   % preconditions
     [on(shakey,B)],                                 % delete
     [on(shakey,floor)]                              % add
     ).

% turnOn
act( turnOn(S),                                                               % name
     [in(shakey,X), in(B,X), on(shakey,B), switch(S), in(S,X), lightOff(X)],  % preconditions
     [lightOff(X)],                                                           % delete
     [lightOn(X)]                                                             % add
     ).

% turnOff
act( turnOff(S),                                                             % name
     [in(shakey,X), in(B,X), on(shakey,B), switch(S), in(S,X), lightOn(X)],  % preconditions
     [lightOn(X)],                                                           % delete
     [lightOff(X)]                                                           % add
     ).

% Goal state
% in(shakey,room1), lightOff(room1), in(box2,room2)
goal_state([in(shakey,room1), lightOff(room1), in(box2,room2)]).

% Initial state
initial_state(
     [      % Shakey
            in(shakey,room3),
            on(shakey,floor),

            % Rooms
            room(room1),
            room(room2),
            room(room3),
            room(room4),

            % Room connections
            connected(room1,room2),
            connected(room1,room3),
            connected(room1,room4),

            connected(room2,room1),
            connected(room2,room3),
            connected(room2,room4),

            connected(room3,room1),
            connected(room3,room2),
            connected(room3,room4),

            connected(room4,room1),
            connected(room4,room2),
            connected(room4,room3),

            % Light switches
            switch(switch1),
            switch(switch2),
            switch(switch3),
            switch(switch4),
            
            % Light status
            lightOn(room1),
            lightOff(room2),
            lightOff(room3),
            lightOn(room4),

            % Light switch locations
            in(switch1,room1),
            in(switch2,room2),
            in(switch3,room3),
            in(switch4,room4),

            % Boxes
            box(box1),
            box(box2),
            box(box3),
            box(box4),

            % Box locations
            in(box1,room1),
            in(box2,room1),
            in(box3,room1),
            in(box4,room1)
     ]).
