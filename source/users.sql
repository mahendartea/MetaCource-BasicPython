CREATE TABLE `users` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `two_factor_secret` text COLLATE utf8mb4_unicode_ci,
  `two_factor_recovery_codes` text COLLATE utf8mb4_unicode_ci,
  `two_factor_confirmed_at` timestamp NULL DEFAULT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `current_team_id` bigint unsigned DEFAULT NULL,
  `profile_photo_path` varchar(2048) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `users` (`id`, `name`, `email`, `email_verified_at`, `password`, `two_factor_secret`, `two_factor_recovery_codes`, `two_factor_confirmed_at`, `remember_token`, `current_team_id`, `profile_photo_path`, `created_at`, `updated_at`) VALUES
(1, 'Mahendar Dwi Payana', 'hendartea@gmail.com', '2024-04-18 04:17:23', '$2y$12$0elOFM4JCnZ/6u9A8whYx.7tl3zUqf1KXvVdWCHjbWDhtgCDzbSYO', NULL, NULL, NULL, NULL, NULL, 'profile-photos/lDgmxC9U2fbHqiW2y4CekGuDOan4EkouPN7gZAB1.jpg', '2024-04-18 04:17:23', '2024-04-18 13:25:21'),
(2, 'Mahendar', 'mahendar@uui.ac.id', NULL, '$2y$12$zIpN3bwdLtvyaT9tcTZncuVo4fug2.qIqt7FEUu.zi0d/bL8.IWta', NULL, NULL, NULL, NULL, NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(3, 'Participant', 'participant@example.com', NULL, '$2y$12$azVy3giyCG4CZaB8bH9f3OAa6o04RbgM8/jepfCXLNMWHi7x0DAXa', NULL, NULL, NULL, NULL, NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(4, 'Enrico Gleason', 'lulu12@example.org', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'OpOhaVY0uV', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(5, 'Mrs. Carmela Denesik', 'lorena.schoen@example.com', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, '0Oc5xTYcct', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(6, 'Kole Wiegand', 'reynold49@example.org', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'jAuE0VmFeW', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(7, 'Jeramie Zboncak', 'lubowitz.donnie@example.net', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'YKJyGjJjcx', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(8, 'Prof. Wellington McKenzie', 'immanuel73@example.com', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'aRXwIUb1s2', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(9, 'Amelia Corwin', 'rwalker@example.net', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'v5vhC1J1V1', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(10, 'Heber Hickle', 'ucrooks@example.net', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'TkNpzPBQzb', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(11, 'Ms. Myrtis Cole', 'pkuphal@example.net', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'ZoEAGUD821', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23'),
(12, 'Mrs. Josie Thompson', 'harber.everardo@example.org', '2024-04-18 04:17:23', '$2y$12$eS/tE3V8KnnmGP7AQFQN9eVOfwLytRUBJXnImPaXPVlBKNvxw9LhW', NULL, NULL, NULL, 'n06B8lW8dI', NULL, NULL, '2024-04-18 04:17:23', '2024-04-18 04:17:23');

