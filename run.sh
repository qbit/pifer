#!/bin/sh

tmux -2 new-session -d -s "pifer"
tmux split-window -v
tmux select-pane -t 0
tmux send-keys "cd html && python -mSimpleHTTPServer" C-m
tmux select-pane -t 1
tmux send-keys "python3 ./pifer.py" C-m
tmux -2 attach-session -t "pifer"
