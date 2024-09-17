create table playground.shares_kb
(
    id           int auto_increment
        primary key,
    prompt       text                                  not null,
    completion   longtext                              null,
    keywords     text                                  null,
    last_updated timestamp default current_timestamp() not null on update current_timestamp(),
    constraint shares_kb_pk
        unique (prompt) using hash
);

