#
# ~/.bashrc
#

[[ $- != *i* ]] && return

colors() {
	local fgc bgc vals seq0

	printf "Color escapes are %s\n" '\e[${value};...;${value}m'
	printf "Values 30..37 are \e[33mforeground colors\e[m\n"
	printf "Values 40..47 are \e[43mbackground colors\e[m\n"
	printf "Value  1 gives a  \e[1mbold-faced look\e[m\n\n"

	# foreground colors
	for fgc in {30..37}; do
		# background colors
		for bgc in {40..47}; do
			fgc=${fgc#37} # white
			bgc=${bgc#40} # black

			vals="${fgc:+$fgc;}${bgc}"
			vals=${vals%%;}

			seq0="${vals:+\e[${vals}m}"
			printf "  %-9s" "${seq0:-(default)}"
			printf " ${seq0}TEXT\e[m"
			printf " \e[${vals:+${vals+$vals;}}1mBOLD\e[m"
		done
		echo; echo
	done
}

[ -r /usr/share/bash-completion/bash_completion ] && . /usr/share/bash-completion/bash_completion

# Change the window title of X terminals
case ${TERM} in
	xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|interix|konsole*)
		PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
		;;
	screen*)
		PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
		;;
esac

use_color=true

# Set colorful PS1 only on colorful terminals.
# dircolors --print-database uses its own built-in database
# instead of using /etc/DIR_COLORS.  Try to use the external file
# first to take advantage of user additions.  Use internal bash
# globbing instead of external grep binary.
safe_term=${TERM//[^[:alnum:]]/?}   # sanitize TERM
match_lhs=""
[[ -f ~/.dir_colors   ]] && match_lhs="${match_lhs}$(<~/.dir_colors)"
[[ -f /etc/DIR_COLORS ]] && match_lhs="${match_lhs}$(</etc/DIR_COLORS)"
[[ -z ${match_lhs}    ]] \
	&& type -P dircolors >/dev/null \
	&& match_lhs=$(dircolors --print-database)
[[ $'\n'${match_lhs} == *$'\n'"TERM "${safe_term}* ]] && use_color=true

if ${use_color} ; then
	# Enable colors for ls, etc.  Prefer ~/.dir_colors #64489
	if type -P dircolors >/dev/null ; then
		if [[ -f ~/.dir_colors ]] ; then
			eval $(dircolors -b ~/.dir_colors)
		elif [[ -f /etc/DIR_COLORS ]] ; then
			eval $(dircolors -b /etc/DIR_COLORS)
		fi
	fi

	if [[ ${EUID} == 0 ]] ; then
		PS1='\[\033[01;31m\][\h\[\033[01;36m\] \W\[\033[01;31m\]]\$\[\033[00m\] '
	else
		PS1='\[\033[01;32m\][\u@\h\[\033[01;37m\] \W\[\033[01;32m\]]\$\[\033[00m\] '
	fi

	alias ls='ls --color=auto'
	alias grep='grep --colour=auto'
	alias egrep='egrep --colour=auto'
	alias fgrep='fgrep --colour=auto'
else
	if [[ ${EUID} == 0 ]] ; then
		# show root@ when we don't have colors
		PS1='\u@\h \W \$ '
	else
		PS1='\u@\h \w \$ '
	fi
fi

unset use_color safe_term match_lhs sh

alias cp="cp -i"                          # confirm before overwriting something
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
alias np='nano -w PKGBUILD'
alias more=less

xhost +local:root > /dev/null 2>&1

complete -cf sudo

# Bash won't get SIGWINCH if another process is in the foreground.
# Enable checkwinsize so that bash will check the terminal size when
# it regains control.  #65623
# http://cnswww.cns.cwru.edu/~chet/bash/FAQ (E11)
shopt -s checkwinsize

shopt -s expand_aliases

# export QT_SELECT=4

# Enable history appending instead of overwriting.  #139609
shopt -s histappend

#
# # ex - archive extractor
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

# custom env var
export EDITOR=/usr/bin/micro

# custom aliases
alias ll="exa -la"
# alias code="codium"
alias pentablet="/usr/lib/pentablet/pentablet.sh &"
alias py="python3"
alias pyenv="source env/bin/activate"
alias colclip="colorpicker --short --one-shot | xclip -selection clipboard"
alias music-dl='youtube-dl -cio "~/Music/%(playlist_uploader)s-%(playlist_title)s/%(playlist_index)02d_%(title)s.%(ext)s" --extract-audio --audio-format mp3'
alias bulk-rename='vimv'
alias sc='search-code'
alias mc='micro'
alias jadwal='kitty +kitten icat $HOME/Pictures/jadwal-kuliah.png'
alias img='kitty +kitten icat'
alias todo='micro $HOME/todo.md'
alias yt='ytfzf -t --detach'

# cd shortcut
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias .......="cd ../../../../../.."
alias ........="cd ../../../../../../.."
alias .........="cd ../../../../../../../.."
alias ..........="cd ../../../../../../../../.."
alias ...........="cd ../../../../../../../../../.."
alias ............="cd ../../../../../../../../../../.."
alias .............="cd ../../../../../../../../../../../.."

# git aliases
alias g="git"
alias gf="git fuzzy status"
alias lg="lazygit"
alias gadd="git add"
alias gcomm="git commit -m"
alias gstat="git status --short"
alias gpush="git push"
alias glog="git log --oneline"
alias gcek="git checkout"

# project aliases
function sr {
	export anchor=`exec pwd`
}
function gr {
    cd $anchor
}

rmd() {
  pandoc $1 | lynx -stdin
}

pandocwatch() {
	ls -d $1 | entr -r pandoc --citeproc --pdf-engine=xelatex $1 -o $2
}

# starship prompt
eval "$(starship init bash)"

# bat
export BAT_STYLE=full
export BAT_THEME="Monokai Extended Bright"

# fzf
[ -f ~/.fzf.bash ] && source ~/.fzf.bash

# git fuzzy

export PATH="/home/jahnsmichael/repos/git-fuzzy/bin:$PATH"
export GF_VERTICAL_THRESHOLD="4.0"

# use __WIDTH__ for horizontal scenarios
# export GF_HORIZONTAL_PREVIEW_PERCENT_CALCULATION='max(50, min(80, 100 - (7000 / __WIDTH__)))'

# use __HEIGHT__ for horizontal scenarios
# export GF_VERTICAL_PREVIEW_PERCENT_CALCULATION='max(50, min(80, 100 - (5000 / __HEIGHT__)))'

# broot
source /home/jahnsmichael/.config/broot/launcher/bash/br

# fzf scripts
export FZF_DEFAULT_OPTS='--layout=reverse --border'

# Install packages using yay
ins() {
    yay -Slq | fzf -q "$1" -m --preview 'yay -Si {1}'| xargs -ro yay -S
}

# Remove installed packages
rem() {
    yay -Qq | fzf -q "$1" -m --preview 'yay -Qi {1}' | xargs -ro yay -Rns
}

# fzf-bash-completion
# source /home/jahnsmichael/repos/fzf-tab-completion/bash/fzf-bash-completion.sh
# bind -x '"\t": fzf_bash_completion'

_fzf_complete_gadd() {
    _fzf_complete --multi --reverse --prompt="gadd> " -- "$@" < <(
		git ls-files -m -o --exclude-standard
	)
}

[ -n "$BASH" ] && complete -F _fzf_complete_gadd -o default -o bashdefault gadd

_fzf_complete_gcek() {
    _fzf_complete --reverse --prompt="gcek> " -- "$@" < <(
		git branch | cut -c 3-
	)
}

[ -n "$BASH" ] && complete -F _fzf_complete_gcek -o default -o bashdefault gcek

# fff
f() {
    fff "$@"
    cd "$(cat "${XDG_CACHE_HOME:=${HOME}/.cache}/fff/.fff_d")"
}

# startup
# colorscript random
# bat -P $HOME/todo.md

# Git Bare
alias cfg='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias lcfg='/usr/bin/lazygit --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias cfgf='cfg fuzzy status'

# pass
export PASSWORD_STORE_ENABLE_EXTENSIONS=true

# sdkman
#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
