#kills a process named killmenow.

exec {'kill_a_process':
    command  => 'pkill killmenow',
    provider => 'shell',
}
