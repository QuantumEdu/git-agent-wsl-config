if status is-interactive
    if test -n "$WARP_BOOTSTRAPPED"; or test -n "$WARP_USE_SSH_WRAPPER"
        set -g fish_term24bit 1
        set -g fish_ambiguous_width 1
        set -g fish_emoji_width 2
    end

    if not functions -q fisher
        curl -sL https://git.io/fisher | source
        fisher install jorgebucaran/fisher
    end
end

set -l IS_TERMUX 0
if test -n "$TERMUX_VERSION"; or test -d /data/data/com.termux
    set IS_TERMUX 1
end

if test $IS_TERMUX -eq 1
    set -x PATH $PREFIX/bin $HOME/.local/bin $HOME/.cargo/bin $PATH
else if test (uname) = Darwin
    if test -f /opt/homebrew/bin/brew
        set BREW_BIN /opt/homebrew/bin/brew
    else if test -f /usr/local/bin/brew
        set BREW_BIN /usr/local/bin/brew
    end
    set -x PATH $HOME/.local/bin $HOME/.opencode/bin $HOME/.volta/bin $HOME/.bun/bin $HOME/.nix-profile/bin /nix/var/nix/profiles/default/bin /usr/local/bin $HOME/.config $HOME/.cargo/bin /usr/local/lib/* $PATH
else
    set BREW_BIN /home/linuxbrew/.linuxbrew/bin/brew
    set -x PATH $HOME/.local/bin $HOME/.opencode/bin $HOME/.volta/bin $HOME/.bun/bin $HOME/.nix-profile/bin /nix/var/nix/profiles/default/bin /usr/local/bin $HOME/.config $HOME/.cargo/bin /usr/local/lib/* $PATH
end

if test $IS_TERMUX -eq 0; and set -q BREW_BIN; and test -f $BREW_BIN
    eval ($BREW_BIN shellenv)
end

# Auto-start tmux only in interactive sessions with a real TTY
if status is-interactive
    if test -t 0; and not set -q TMUX
        tmux new-session -A -s main
    end
end

starship init fish | source
zoxide init fish | source
atuin init fish | source
fzf --fish | source

set -x PATH $HOME/.cargo/bin $PATH

set -Ux CARAPACE_BRIDGES 'zsh,fish,bash,inshellisense'
set -l CARAPACE_CACHE ~/.cache/carapace/carapace.fish

if not test -d ~/.cache/carapace
    mkdir -p ~/.cache/carapace
end

set -l regen_cache 0
if not test -f $CARAPACE_CACHE
    set regen_cache 1
else if test (find $CARAPACE_CACHE -mtime +7 2>/dev/null)
    set regen_cache 1
end

if test $regen_cache -eq 1
    carapace _carapace fish > $CARAPACE_CACHE 2>/dev/null
end

if test -f $CARAPACE_CACHE; and test -s $CARAPACE_CACHE
    source $CARAPACE_CACHE
end

set -g fish_greeting ""

fish_vi_key_bindings

set -gx EDITOR nvim
set -gx VISUAL nvim

if test (uname) = Darwin
    alias ls='ls --color=auto'
else
    alias ls='gls --color=auto'
end

# Yazi shell wrapper — cd on quit
function y
	set tmp (mktemp -t "yazi-cwd.XXXXXX")
	command yazi $argv --cwd-file=$tmp
	if set cwd (command cat $tmp); and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
		builtin cd -- "$cwd"
	end
	command rm -f -- "$tmp"
end

alias fzfbat='fzf --preview="bat --theme=gruvbox-dark --color=always {}"'
alias fzfnvim='nvim (fzf --preview="bat --theme=gruvbox-dark --color=always {}")'

set -l foreground F3F6F9 normal
set -l selection 263356 normal
set -l comment 8394A3 brblack
set -l red CB7C94 red
set -l orange DEBA87 orange
set -l yellow FFE066 yellow
set -l green B7CC85 green
set -l purple A3B5D6 purple
set -l cyan 7AA89F cyan
set -l pink FF8DD7 magenta

set -g fish_color_normal $foreground
set -g fish_color_command $cyan
set -g fish_color_keyword $pink
set -g fish_color_quote $yellow
set -g fish_color_redirection $foreground
set -g fish_color_end $orange
set -g fish_color_error $red
set -g fish_color_param $purple
set -g fish_color_comment $comment
set -g fish_color_selection --background=$selection
set -g fish_color_search_match --background=$selection
set -g fish_color_operator $green
set -g fish_color_escape $pink
set -g fish_color_autosuggestion $comment

set -g fish_pager_color_progress $comment
set -g fish_pager_color_prefix $cyan
set -g fish_pager_color_completion $foreground
set -g fish_pager_color_description $comment