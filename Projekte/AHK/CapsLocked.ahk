Capslock::/


Control & CapsLock::
       GetKeyState CapsLockState, CapsLock, T
       IfEqual CapsLockState,D, SetCapslockState, AlwaysOff
    Else SetCapslockState AlwaysOn
Return