CREATE TABLE `admincredentials` (
  `username` varchar(100) NOT NULL,
  `password` varchar(8) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phno` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `adminreply` (
  `ebid` varchar(100) NOT NULL,
  `msg` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `customermessage` (
  `ebid` varchar(100) NOT NULL,
  `message` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `customerregistration` (
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `ebid` varchar(10) NOT NULL,
  `phno` int(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `village` varchar(50) NOT NULL,
  `proof` blob NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `estimation` (
  `ebid` varchar(100) NOT NULL,
  `month` varchar(100) NOT NULL,
  `units` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `paymentdetails` (
  `ebid` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `msg` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



