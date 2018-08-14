-- Creates a view with view count per article's title and author. This is done
-- by agreggating view count, grouping by slug in logs table and joining it
-- with articles and authors tables on slug and id.

CREATE OR REPLACE VIEW viewcount_article_author AS
SELECT view_count, title AS article_title, name AS author_name
FROM (SELECT substring(path, 10) as article_slug, count(status) as view_count
FROM log
WHERE status like '200%' AND path LIKE '/article/%'
GROUP BY article_slug) as view_count_per_title
JOIN (SELECT slug, author, title from articles) artcls
ON view_count_per_title.article_slug = artcls.slug
JOIN (SELECT name, id FROM authors) athr
ON athr.id = artcls.author;


-- Creates a view with status date, total statuses count, and total errors
-- count. This is done by counting all statuses, counting only error statuses,
-- grouping by time stamp, and joining both counts on time stamp.

CREATE OR REPLACE VIEW status_count AS
SELECT time_stamp_a AS status_date, total_statuses, total_errors
FROM (SELECT time::date AS time_stamp_a, count(status) AS total_statuses
FROM log
GROUP BY time_stamp_a) all_statuses
JOIN (SELECT time::date AS time_stamp_b, count(status) AS total_errors
FROM log
WHERE status LIKE '404%' 
GROUP BY time_stamp_b) error_statuses
ON all_statuses.time_stamp_a = error_statuses.time_stamp_b;


-- Creates a view with status date, total status count and total error count

CREATE OR REPLACE VIEW date_error_count AS
SELECT status_date, total_statuses, total_errors
FROM status_count
WHERE total_errors > (total_statuses * 0.01);


-- Creates a view with status_date and error_rate:

CREATE OR REPLACE VIEW error_rate_perc AS
SELECT status_date, CAST(total_errors AS FLOAT) / CAST(total_statuses AS FLOAT)
* 100 AS error_rate
FROM date_error_count;