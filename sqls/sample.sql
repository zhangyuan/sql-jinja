{% set user_type = 1 %}
SELECT
  *
FROM
  users
WHERE
  user_type = {{ user_type }} AND updated_at < '{{ logical_date }}'
